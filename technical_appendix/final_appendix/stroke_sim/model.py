"""Occupancy-audit simulation model for the stroke pathway."""

from __future__ import annotations

from dataclasses import dataclass, field
import random

import pandas as pd
import simpy

from .config import Destination, SimulationSettings, Ward
from .distributions import lognormal_mu_sigma_from_mean_sd
from .parameters import (
    ACUTE_ARRIVAL_MEAN_DAYS,
    BASE_CAPACITY_BEDS,
    LENGTH_OF_STAY,
    REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS,
    ROUTING_FROM_ACUTE,
    ROUTING_FROM_REHAB,
)
from .patients import PatientGroup


def _normalise_probabilities(probabilities: dict[Destination, float]) -> dict[Destination, float]:
    total = sum(probabilities.values())
    return {key: value / total for key, value in probabilities.items()}


@dataclass(frozen=True)
class ModelResult:
    daily_audit: pd.DataFrame
    metadata: dict[str, float | int]


@dataclass
class StrokePathwayModel:
    """Parameter-driven occupancy audit model.

    This first implementation follows the paper's unfettered-demand idea:
    patients are never blocked, and daily occupancy is audited for later
    probability-of-delay calculations.
    """

    settings: SimulationSettings
    random_seed: int = 42
    _env: simpy.Environment = field(init=False, repr=False)
    _rng: random.Random = field(init=False, repr=False)
    _acute_occupancy: int = field(init=False, default=0)
    _acute_stroke_occupancy: int = field(init=False, default=0)
    _rehab_occupancy: int = field(init=False, default=0)
    _audit_rows: list[dict[str, int | float]] = field(init=False, default_factory=list, repr=False)

    def __post_init__(self) -> None:
        self._env = simpy.Environment()
        self._rng = random.Random(self.random_seed)

    def run(self) -> ModelResult:
        self._schedule_arrivals()
        self._env.process(self._daily_audit())
        final_time = self.settings.warm_up_days + self.settings.run_length_days
        self._env.run(until=final_time)
        daily_audit = pd.DataFrame(self._audit_rows)
        return ModelResult(
            daily_audit=daily_audit,
            metadata={
                "random_seed": self.random_seed,
                "warm_up_days": self.settings.warm_up_days,
                "run_length_days": self.settings.run_length_days,
                "acute_beds": BASE_CAPACITY_BEDS[Ward.ACUTE],
                "rehab_beds": BASE_CAPACITY_BEDS[Ward.REHAB],
            },
        )

    def _schedule_arrivals(self) -> None:
        for patient_group, parameter in ACUTE_ARRIVAL_MEAN_DAYS.items():
            if patient_group.value in self.settings.excluded_patient_groups:
                continue
            self._env.process(self._acute_arrival_stream(patient_group, parameter.mean_interarrival_days))
        for patient_group, parameter in REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS.items():
            if patient_group.value in self.settings.excluded_patient_groups:
                continue
            self._env.process(self._rehab_external_arrival_stream(patient_group, parameter.mean_interarrival_days))

    def _acute_arrival_stream(self, patient_group: PatientGroup, mean_interarrival_days: float) -> simpy.events.Event:
        while True:
            adjusted_mean = mean_interarrival_days / self.settings.arrival_rate_multiplier
            interarrival = self._rng.expovariate(1.0 / adjusted_mean)
            yield self._env.timeout(interarrival)
            self._env.process(self._patient_from_acute_arrival(patient_group))

    def _rehab_external_arrival_stream(self, patient_group: PatientGroup, mean_interarrival_days: float) -> simpy.events.Event:
        while True:
            adjusted_mean = mean_interarrival_days / self.settings.arrival_rate_multiplier
            interarrival = self._rng.expovariate(1.0 / adjusted_mean)
            yield self._env.timeout(interarrival)
            self._env.process(self._patient_from_rehab_external_arrival(patient_group))

    def _patient_from_acute_arrival(self, patient_group: PatientGroup) -> simpy.events.Event:
        self._acute_occupancy += 1
        if patient_group is PatientGroup.STROKE:
            self._acute_stroke_occupancy += 1
        acute_destination = self._sample_destination(ROUTING_FROM_ACUTE[patient_group])
        acute_profile = self._choose_acute_profile(patient_group, acute_destination)
        yield self._env.timeout(self._sample_los(Ward.ACUTE, acute_profile))
        self._acute_occupancy -= 1
        if patient_group is PatientGroup.STROKE:
            self._acute_stroke_occupancy -= 1
        if acute_destination is Destination.REHAB:
            self._env.process(self._rehab_stay(patient_group))

    def _patient_from_rehab_external_arrival(self, patient_group: PatientGroup) -> simpy.events.Event:
        self._env.process(self._rehab_stay(patient_group))
        yield self._env.timeout(0)

    def _rehab_stay(self, patient_group: PatientGroup) -> simpy.events.Event:
        self._rehab_occupancy += 1
        rehab_destination = self._sample_destination(ROUTING_FROM_REHAB[patient_group])
        rehab_profile = self._choose_rehab_profile(patient_group, rehab_destination)
        yield self._env.timeout(self._sample_los(Ward.REHAB, rehab_profile))
        self._rehab_occupancy -= 1

    def _daily_audit(self) -> simpy.events.Event:
        while True:
            yield self._env.timeout(self.settings.audit_interval_days)
            if self._env.now <= self.settings.warm_up_days:
                continue
            self._audit_rows.append(
                {
                    "day": int(self._env.now - self.settings.warm_up_days),
                    "acute_occupancy": self._acute_occupancy,
                    "acute_stroke_occupancy": self._acute_stroke_occupancy,
                    "rehab_occupancy": self._rehab_occupancy,
                }
            )

    def _choose_acute_profile(self, patient_group: PatientGroup, destination: Destination) -> str:
        if patient_group is PatientGroup.STROKE:
            if destination is Destination.ESD:
                return "stroke_esd"
            return "stroke_no_esd"
        return patient_group.value

    def _choose_rehab_profile(self, patient_group: PatientGroup, destination: Destination) -> str:
        if patient_group is PatientGroup.STROKE:
            if destination is Destination.ESD:
                return "stroke_esd"
            return "stroke_no_esd"
        return patient_group.value

    def _sample_destination(self, probabilities: dict[Destination, float]) -> Destination:
        normalised = _normalise_probabilities(probabilities)
        threshold = self._rng.random()
        cumulative = 0.0
        last_destination = next(iter(normalised))
        for destination, probability in normalised.items():
            cumulative += probability
            last_destination = destination
            if threshold <= cumulative:
                return destination
        return last_destination

    def _sample_los(self, ward: Ward, profile: str) -> float:
        summary = LENGTH_OF_STAY[ward][profile]
        mu, sigma = lognormal_mu_sigma_from_mean_sd(summary.mean, summary.sd)
        return self._rng.lognormvariate(mu, sigma)
