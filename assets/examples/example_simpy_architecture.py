"""
Example of Core SimPy architecture template (Python 3.11 / SimPy 4.x)

Source ChatGPT 5.2

Design goals:
- All parameters in a Scenario container
- Patient = a SimPy process
- Distributions are objects (seedable)
- Model runner handles replications + metrics
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, List
import math
import numpy as np
import simpy

# -------------------------
# Debug / tracing utility
# -------------------------

TRACE = False

def trace(env: simpy.Environment, msg: str) -> None:
    if TRACE:
        print(f"[t={env.now:8.2f}] {msg}")


# -------------------------
# Distribution helpers
# -------------------------

class Exponential:
    """Exponential distribution parameterised by mean."""
    def __init__(self, mean: float, random_seed: Optional[int] = None):
        if mean <= 0:
            raise ValueError("mean must be > 0")
        self.mean = mean
        self.rng = np.random.default_rng(random_seed)

    def sample(self) -> float:
        return float(self.rng.exponential(self.mean))


class Lognormal:
    """
    Lognormal distribution parameterised by underlying normal mu, sigma
    (i.e., if X ~ Lognormal(mu, sigma), then ln(X) ~ Normal(mu, sigma)).
    """
    def __init__(self, mu: float, sigma: float, random_seed: Optional[int] = None):
        if sigma <= 0:
            raise ValueError("sigma must be > 0")
        self.mu = mu
        self.sigma = sigma
        self.rng = np.random.default_rng(random_seed)

    def sample(self) -> float:
        return float(self.rng.lognormal(mean=self.mu, sigma=self.sigma))


# -------------------------
# Scenario (parameter container)
# -------------------------

@dataclass
class Scenario:
    # Arrivals (e.g., Poisson process)
    mean_iat_min: float = 8.0  # mean inter-arrival time in minutes

    # Pathway activity-time distributions (replace with paper parameters)
    t_pre_hosp_mu: float = math.log(30)  # placeholder
    t_pre_hosp_sigma: float = 0.3
    t_in_hosp_mu: float = math.log(60)   # placeholder
    t_in_hosp_sigma: float = 0.35

    # Replication config
    random_seed: int = 42
    run_until_min: float = 24 * 60  # 1 day in minutes
    warm_up_min: float = 0.0        # set if you later need warm-up

    def build_distributions(self) -> Dict[str, object]:
        """
        Central place to create seedable distribution instances.
        Use different seeds per distribution for stability/reproducibility.
        """
        return {
            "iat": Exponential(self.mean_iat_min, random_seed=self.random_seed + 1),
            "pre_hosp": Lognormal(self.t_pre_hosp_mu, self.t_pre_hosp_sigma, random_seed=self.random_seed + 2),
            "in_hosp": Lognormal(self.t_in_hosp_mu, self.t_in_hosp_sigma, random_seed=self.random_seed + 3),
        }


# -------------------------
# Patient process
# -------------------------

class Patient:
    def __init__(self, env: simpy.Environment, pid: int, dists: Dict[str, object], results: List[dict]):
        self.env = env
        self.pid = pid
        self.dists = dists
        self.results = results

    def execute(self):
        t_arrival = self.env.now
        trace(self.env, f"Patient {self.pid} arrived")

        # Stage 1: pre-hospital
        pre = self.dists["pre_hosp"].sample()
        yield self.env.timeout(pre)
        trace(self.env, f"Patient {self.pid} finished pre-hospital (+{pre:.1f} min)")

        # Stage 2: in-hospital
        inh = self.dists["in_hosp"].sample()
        yield self.env.timeout(inh)
        trace(self.env, f"Patient {self.pid} finished in-hospital (+{inh:.1f} min)")

        t_complete = self.env.now

        # Store outputs (simple dict; easy to convert to DataFrame later)
        self.results.append({
            "pid": self.pid,
            "t_arrival": t_arrival,
            "t_complete": t_complete,
            "los_total": t_complete - t_arrival,
            "pre_hosp": pre,
            "in_hosp": inh,
        })


# -------------------------
# Arrival generator
# -------------------------

def patient_arrivals(env: simpy.Environment, scenario: Scenario, dists: Dict[str, object], results: List[dict]):
    pid = 0
    while True:
        iat = dists["iat"].sample()
        yield env.timeout(iat)

        pid += 1
        patient = Patient(env, pid=pid, dists=dists, results=results)
        env.process(patient.execute())


# -------------------------
# Model runner
# -------------------------

class Model:
    def __init__(self, scenario: Scenario):
        self.scenario = scenario

    def run(self) -> List[dict]:
        env = simpy.Environment()
        dists = self.scenario.build_distributions()
        results: List[dict] = []

        env.process(patient_arrivals(env, self.scenario, dists, results))
        env.run(until=self.scenario.run_until_min)

        # Optional warm-up filtering (if you later introduce it)
        if self.scenario.warm_up_min > 0:
            results = [r for r in results if r["t_arrival"] >= self.scenario.warm_up_min]

        return results


# -------------------------
# Example usage
# -------------------------

if __name__ == "__main__":
    scenario = Scenario(
        mean_iat_min=8.0,
        # replace placeholders with paper parameters
        t_pre_hosp_mu=math.log(30),
        t_pre_hosp_sigma=0.3,
        t_in_hosp_mu=math.log(60),
        t_in_hosp_sigma=0.35,
        random_seed=123,
        run_until_min=24 * 60,
    )

    model = Model(scenario)
    results = model.run()
    print(f"Simulated patients completed: {len(results)}")
    if results:
        mean_los = sum(r["los_total"] for r in results) / len(results)
        print(f"Mean total time (min): {mean_los:.1f}")