"""Configuration objects for model parameters."""

from dataclasses import dataclass
from enum import StrEnum


class Ward(StrEnum):
    ACUTE = "acute_stroke_unit"
    REHAB = "rehab_unit"


class Destination(StrEnum):
    REHAB = "rehab"
    ESD = "esd"
    OTHER = "other"


@dataclass(frozen=True)
class SimulationSettings:
    """Top-level execution settings for a simulation experiment."""

    run_length_days: int = 5 * 365
    warm_up_days: int = 3 * 365
    replications: int = 150
    audit_interval_days: float = 1.0
    arrival_rate_multiplier: float = 1.0
    excluded_patient_groups: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArrivalParameter:
    """Mean inter-arrival time for a patient stream."""

    mean_interarrival_days: float
    source_note: str


@dataclass(frozen=True)
class LognormalSummary:
    """Reported arithmetic summaries for a lognormal LOS distribution."""

    mean: float
    sd: float
    median: float
    p5: float
    p95: float
    p25: float
    p75: float
    source_note: str
