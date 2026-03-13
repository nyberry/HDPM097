"""
Stroke Pathway DES - Iteration 2: Arrivals with Testing (SimPy)
=================================================================
Replicating the model described by Monks et al. (2016)
"A modelling tool for capacity planning in acute and community stroke
services"  BMC Health Services Research, 16, 530.

Python: 3.11+
SimPy:  4.1.1

Install dependencies:
    pip install simpy numpy pandas scipy

This iteration covers Steps 1 & 2 of the iterative development:
  Step 1: Generate patient arrivals for four categories using SimPy
  Step 2: Test the arrival processes

Key parameters from the paper (Fig. 2 and main text):
  - Stroke:               mean IAT = 1.2 days  (n=1320 per year)
  - TIA:                  mean IAT = 9.3 days  (n=158 per year)
  - Complex neurological: mean IAT = 3.6 days  (n=456 per year)
  - Other:                mean IAT = 3.2 days  (n=510 per year)

  - Run length:    5 years (results collection period)
  - Warm-up:       3 years
  - Replications:  150

Inter-arrival times use exponential distributions (implying random/Poisson
arrivals) as stated in the paper's Statistical Analysis section.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import Optional, Sequence

import numpy as np
import pandas as pd
import simpy
from scipy import stats


# ---------------------------------------------------------------------------
# Tracing utility
# ---------------------------------------------------------------------------

TRACE = False  # Set True to enable per-event console output


def trace(msg: str) -> None:
    """Conditionally print a simulation trace message."""
    if TRACE:
        print(msg)


# ---------------------------------------------------------------------------
# Distribution classes
# ---------------------------------------------------------------------------

class Distribution:
    """
    Base class for seedable probability distributions.

    Handles the common pattern of creating a per-instance NumPy
    Generator from an optional random seed.  Subclasses implement
    sample() with distribution-specific logic.
    """

    def __init__(self, random_seed: Optional[int] = None) -> None:
        self.rng = np.random.default_rng(random_seed)

    def sample(self) -> float:
        raise NotImplementedError


class Exponential(Distribution):
    """
    Exponential distribution parameterised by the mean (scale).

    Used for inter-arrival times in the Monks et al. model.

    Parameters
    ----------
    mean : float
        Mean of the exponential distribution (must be > 0).
    random_seed : int, optional
        Seed for the random number generator.
    """

    def __init__(self, mean: float, random_seed: Optional[int] = None) -> None:
        if mean <= 0:
            raise ValueError(f"Exponential mean must be > 0, got {mean}")
        super().__init__(random_seed=random_seed)
        self.mean = float(mean)

    def sample(self) -> float:
        """Draw a single sample from the distribution."""
        return float(self.rng.exponential(scale=self.mean))


class Lognormal(Distribution):
    """
    Lognormal distribution parameterised by mu and sigma of the
    underlying normal distribution.

    Used for length-of-stay distributions in the Monks et al. model.
    Will be used in later iterations when acute/rehab wards are added.

    Parameters
    ----------
    mu : float
        Mean of the underlying normal distribution.
    sigma : float
        Standard deviation of the underlying normal (must be > 0).
    random_seed : int, optional
        Seed for the random number generator.
    """

    def __init__(
        self, mu: float, sigma: float, random_seed: Optional[int] = None
    ) -> None:
        if sigma <= 0:
            raise ValueError(f"Lognormal sigma must be > 0, got {sigma}")
        super().__init__(random_seed=random_seed)
        self.mu = float(mu)
        self.sigma = float(sigma)

    def sample(self) -> float:
        """Draw a single sample from the distribution."""
        return float(self.rng.lognormal(mean=self.mu, sigma=self.sigma))


# ---------------------------------------------------------------------------
# Scenario container
# ---------------------------------------------------------------------------

@dataclass
class Scenario:
    """
    Container for all simulation model parameters.

    Default values represent the base case from Monks et al. (2016).
    Adjusting parameters creates alternative scenarios as described
    in Table 1 of the paper.
    """

    # --- Random number control ---
    random_seed: int = 42

    # --- Patient categories (stable ordering for reproducibility) ---
    categories: tuple[str, ...] = (
        "stroke", "tia", "complex_neuro", "other"
    )

    # --- Arrival parameters ---
    # Mean inter-arrival time in days (from Fig. 2 of Monks et al.)
    mean_iat_days: dict[str, float] = field(default_factory=lambda: {
        "stroke": 1.2,
        "tia": 9.3,
        "complex_neuro": 3.6,
        "other": 3.2,
    })

    # Base-period annual patient counts (from main text, for validation)
    base_period_counts: dict[str, int] = field(default_factory=lambda: {
        "stroke": 1320,
        "tia": 158,
        "complex_neuro": 456,
        "other": 510,
    })

    # --- Simulation run parameters (from paper's Methods section) ---
    # Results collection period in days (5 years)
    results_collection_period: float = 365.0 * 5

    # Warm-up period in days (3 years).
    # For arrivals-only this has minimal effect, but is included for
    # consistency with later iterations involving bed occupancy.
    warm_up_period: float = 365.0 * 3

    # Number of independent replications
    n_reps: int = 150

    def __post_init__(self) -> None:
        """Validate that all category keys are consistent."""
        cat_set = set(self.categories)
        for name, mapping in [
            ("mean_iat_days", self.mean_iat_days),
            ("base_period_counts", self.base_period_counts),
        ]:
            if set(mapping) != cat_set:
                missing = cat_set - set(mapping)
                extra = set(mapping) - cat_set
                raise ValueError(
                    f"{name} keys mismatch. "
                    f"missing={missing}, extra={extra}"
                )
        for cat, iat in self.mean_iat_days.items():
            if iat <= 0:
                raise ValueError(
                    f"mean_iat_days['{cat}'] must be > 0, got {iat}"
                )

    @property
    def total_run_length(self) -> float:
        """Total simulation time: warm-up + results collection (days)."""
        return self.warm_up_period + self.results_collection_period

    def expected_arrivals_per_year(self, category: str) -> float:
        """Theoretical expected annual arrivals for a category."""
        return 365.0 / self.mean_iat_days[category]


# ---------------------------------------------------------------------------
# Patient data class
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Patient:
    """A patient entity flowing through the simulation."""
    id: int
    category: str
    arrival_time: float  # days since simulation clock t=0


# ---------------------------------------------------------------------------
# SimPy arrival process
# ---------------------------------------------------------------------------

def arrival_generator(
    env: simpy.Environment,
    category: str,
    iat_dist: Exponential,
    patients_out: list[Patient],
    id_counter: itertools.count,
) -> None:
    """
    SimPy generator process: produces arrivals for one patient category.

    Each iteration samples an inter-arrival time from the exponential
    distribution, waits that duration via env.timeout(), then creates
    a Patient and appends it to the shared output list.

    The process runs indefinitely and is terminated when the SimPy
    environment reaches its ``until`` time in env.run().

    Parameters
    ----------
    env : simpy.Environment
        The SimPy simulation environment.
    category : str
        Patient category label.
    iat_dist : Exponential
        Inter-arrival time distribution for this category.
    patients_out : list[Patient]
        Shared list where new patients are appended.
    id_counter : itertools.count
        Shared counter for assigning unique patient IDs.
    """
    while True:
        # Sample inter-arrival time and wait
        iat = iat_dist.sample()
        yield env.timeout(iat)

        # Create patient at current simulation time
        pid = next(id_counter)
        patient = Patient(id=pid, category=category, arrival_time=env.now)
        patients_out.append(patient)

        trace(
            f"[t={env.now:8.3f} d] arrival: id={pid:5d}  "
            f"category={category}"
        )


# ---------------------------------------------------------------------------
# Single replication runner
# ---------------------------------------------------------------------------

def run_single_replication(
    scenario: Scenario,
    rep_seed: int,
    categories: Optional[Sequence[str]] = None,
) -> list[Patient]:
    """
    Execute one replication of the arrivals-only model using SimPy.

    Parameters
    ----------
    scenario : Scenario
        Model parameters.
    rep_seed : int
        Seed for this specific replication (used to derive
        per-category stream seeds deterministically).
    categories : sequence of str, optional
        Which categories to include.  Default: all categories in
        the scenario.  Passing a subset supports scenarios such as
        Scenario 4 in the paper (no complex-neurological patients).

    Returns
    -------
    list[Patient]
        Patients arriving during the results collection period
        (i.e. after the warm-up), sorted by arrival time.
    """
    # Determine which categories to simulate
    selected = (
        list(categories) if categories is not None
        else list(scenario.categories)
    )
    unknown = sorted(set(selected) - set(scenario.categories))
    if unknown:
        raise ValueError(
            f"Unknown categories: {unknown}. "
            f"Valid: {list(scenario.categories)}"
        )

    env = simpy.Environment()
    all_patients: list[Patient] = []
    id_counter = itertools.count(start=1)

    # Master RNG derives independent per-category stream seeds.
    # We iterate over ALL scenario categories (not just selected)
    # so that adding/removing a category does not shift the seed
    # sequence for the remaining categories.
    rng_master = np.random.default_rng(rep_seed)

    for cat in scenario.categories:
        stream_seed = int(rng_master.integers(0, 2**31, dtype=np.int64))

        if cat not in selected:
            continue  # skip but seed was still consumed

        iat_dist = Exponential(
            mean=scenario.mean_iat_days[cat],
            random_seed=stream_seed,
        )

        # Register the arrival process with SimPy
        env.process(
            arrival_generator(
                env,
                category=cat,
                iat_dist=iat_dist,
                patients_out=all_patients,
                id_counter=id_counter,
            )
        )

    # Run simulation for warm-up + results collection
    total_time = scenario.total_run_length
    trace(
        f"Rep (seed={rep_seed}): running for {total_time:.0f} days "
        f"(warm-up={scenario.warm_up_period:.0f}d, "
        f"collection={scenario.results_collection_period:.0f}d, "
        f"categories={selected})"
    )
    env.run(until=total_time)

    # Discard warm-up arrivals
    results_patients = [
        p for p in all_patients
        if p.arrival_time >= scenario.warm_up_period
    ]

    # Sort by arrival time (SimPy interleaves categories by event time)
    results_patients.sort(key=lambda p: p.arrival_time)

    # Re-assign sequential IDs after filtering and sorting
    final_patients = [
        Patient(id=i + 1, category=p.category, arrival_time=p.arrival_time)
        for i, p in enumerate(results_patients)
    ]

    trace(
        f"Rep (seed={rep_seed}): {len(all_patients)} total, "
        f"{len(final_patients)} after warm-up"
    )
    return final_patients


# ---------------------------------------------------------------------------
# Summary helper
# ---------------------------------------------------------------------------

def summarise_arrivals(
    patients: list[Patient],
    scenario: Scenario,
) -> dict[str, int]:
    """
    Count arrivals by category.

    Returns a dict keyed by category name with integer counts.
    Categories with zero arrivals (e.g. excluded categories) are
    included with a count of 0.
    """
    counts = {cat: 0 for cat in scenario.categories}
    for p in patients:
        counts[p.category] += 1
    return counts


# ---------------------------------------------------------------------------
# Multiple replications
# ---------------------------------------------------------------------------

def run_replications(
    scenario: Optional[Scenario] = None,
    categories: Optional[Sequence[str]] = None,
) -> pd.DataFrame:
    """
    Run all replications and return a summary DataFrame.

    Each row contains annualised arrival counts per category
    for one replication.

    Parameters
    ----------
    scenario : Scenario, optional
        Model parameters (base case by default).
    categories : sequence of str, optional
        Which categories to simulate. Default: all.

    Returns
    -------
    pd.DataFrame
        Columns: 'rep', one per category (annual count), and 'total'.
    """
    sc = scenario or Scenario()

    # Generate independent replication seeds from the master seed
    rng_reps = np.random.default_rng(sc.random_seed)
    rep_seeds = rng_reps.integers(0, 2**31, size=sc.n_reps, dtype=np.int64)

    years = sc.results_collection_period / 365.0
    records = []

    for i, seed in enumerate(rep_seeds):
        if (i + 1) % 25 == 0 or i == 0:
            print(f"  Replication {i + 1}/{sc.n_reps}...")

        patients = run_single_replication(
            sc, int(seed), categories=categories
        )

        # Count arrivals by category
        counts = summarise_arrivals(patients, sc)

        # Annualise
        row = {"rep": i + 1}
        for cat in sc.categories:
            row[cat] = counts[cat] / years
        row["total"] = sum(counts.values()) / years
        records.append(row)

    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# Testing / validation functions (Step 2)
# ---------------------------------------------------------------------------

def test_arrival_counts(
    results_df: pd.DataFrame,
    scenario: Scenario,
    significance: float = 0.05,
) -> pd.DataFrame:
    """
    Test 1: Mean annual arrivals vs theoretical expectation.

    For each category, checks whether the theoretical expected annual
    count (365 / mean_iat) falls within the 95% confidence interval
    of the simulated mean across replications.
    """
    rows = []
    for cat in scenario.categories:
        sim_values = results_df[cat].values
        sim_mean = np.mean(sim_values)
        sim_std = np.std(sim_values, ddof=1)
        n = len(sim_values)

        expected = scenario.expected_arrivals_per_year(cat)

        # 95% CI for the mean
        t_crit = stats.t.ppf(1 - significance / 2, df=n - 1)
        margin = t_crit * (sim_std / np.sqrt(n))
        ci_low = sim_mean - margin
        ci_high = sim_mean + margin

        within_ci = ci_low <= expected <= ci_high

        rows.append({
            "category": cat,
            "expected_annual": round(expected, 1),
            "sim_mean_annual": round(sim_mean, 1),
            "sim_std": round(sim_std, 1),
            "ci_lower": round(ci_low, 1),
            "ci_upper": round(ci_high, 1),
            "expected_in_ci": within_ci,
            "PASS": within_ci,
        })

    return pd.DataFrame(rows)


def test_arrival_proportions(
    results_df: pd.DataFrame,
    scenario: Scenario,
    tolerance_pp: float = 3.0,
) -> pd.DataFrame:
    """
    Test 2: Category proportions vs base-period proportions.

    The paper reports approximate proportions:
      stroke ~54%, TIA ~6%, complex neuro ~19%, other ~21%.
    Checks that simulated proportions are within a tolerance
    (default 3 percentage points).
    """
    base_total = sum(scenario.base_period_counts.values())

    rows = []
    for cat in scenario.categories:
        expected_prop = scenario.base_period_counts[cat] / base_total
        sim_mean_annual = results_df[cat].mean()
        sim_total_annual = results_df["total"].mean()
        sim_prop = sim_mean_annual / sim_total_annual

        diff_pp = (sim_prop - expected_prop) * 100

        rows.append({
            "category": cat,
            "base_prop": f"{expected_prop:.2%}",
            "sim_prop": f"{sim_prop:.2%}",
            "diff_pp": round(diff_pp, 2),
            "PASS": abs(diff_pp) < tolerance_pp,
        })

    return pd.DataFrame(rows)


def test_exponential_distribution(
    scenario: Scenario,
    n_samples: int = 10_000,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Test 3: Verify the Exponential distribution class produces
    samples with correct statistical properties.

    For Exp(mean=m): E[X] = m, Var(X) = m^2, CV = 1.0.
    """
    rows = []
    rng = np.random.default_rng(seed)

    for cat in scenario.categories:
        stream_seed = int(rng.integers(0, 2**31))
        dist = Exponential(
            mean=scenario.mean_iat_days[cat],
            random_seed=stream_seed,
        )
        samples = np.array([dist.sample() for _ in range(n_samples)])

        expected_mean = scenario.mean_iat_days[cat]
        sample_mean = float(np.mean(samples))
        sample_std = float(np.std(samples, ddof=1))
        cv = sample_std / sample_mean

        # Mean within 5% of expected
        mean_ok = abs(sample_mean - expected_mean) / expected_mean < 0.05
        # CV approximately 1.0 (characteristic of exponential)
        cv_ok = abs(cv - 1.0) < 0.1

        rows.append({
            "category": cat,
            "target_mean": expected_mean,
            "sample_mean": round(sample_mean, 3),
            "sample_std": round(sample_std, 3),
            "cv": round(cv, 3),
            "mean_ok": mean_ok,
            "cv_near_1": cv_ok,
            "PASS": mean_ok and cv_ok,
        })

    return pd.DataFrame(rows)


def test_reproducibility(scenario: Scenario) -> bool:
    """
    Test 4: Same replication seed produces identical patient lists.
    """
    seed = 12345
    patients_a = run_single_replication(scenario, rep_seed=seed)
    patients_b = run_single_replication(scenario, rep_seed=seed)

    if len(patients_a) != len(patients_b):
        return False

    for pa, pb in zip(patients_a, patients_b):
        if pa.category != pb.category:
            return False
        if abs(pa.arrival_time - pb.arrival_time) > 1e-10:
            return False

    return True


def test_no_warm_up_arrivals(scenario: Scenario) -> bool:
    """
    Test 5: Confirm that no patients in the output have an arrival
    time earlier than the warm-up period.
    """
    patients = run_single_replication(scenario, rep_seed=99)
    for p in patients:
        if p.arrival_time < scenario.warm_up_period:
            return False
    return True


def test_category_exclusion(scenario: Scenario) -> bool:
    """
    Test 6: Verify that excluding a category produces zero arrivals
    for that category and does not affect the seeds of other
    categories (i.e. their arrival times remain identical).

    This supports Scenario 4 from the paper (no complex-neurological
    patients).
    """
    seed = 54321

    # Full run: all categories
    patients_full = run_single_replication(scenario, rep_seed=seed)

    # Partial run: exclude complex_neuro
    excluded = "complex_neuro"
    selected = [c for c in scenario.categories if c != excluded]
    patients_partial = run_single_replication(
        scenario, rep_seed=seed, categories=selected
    )

    # Check no excluded patients appear
    for p in patients_partial:
        if p.category == excluded:
            return False

    # Check that non-excluded arrival times match the full run.
    # Because the master RNG consumes a seed per category in the same
    # order regardless of selection, the remaining streams should
    # produce identical arrival times.
    full_by_cat = {}
    for p in patients_full:
        full_by_cat.setdefault(p.category, []).append(p.arrival_time)

    partial_by_cat = {}
    for p in patients_partial:
        partial_by_cat.setdefault(p.category, []).append(p.arrival_time)

    for cat in selected:
        full_times = full_by_cat.get(cat, [])
        partial_times = partial_by_cat.get(cat, [])
        if len(full_times) != len(partial_times):
            return False
        for ft, pt in zip(full_times, partial_times):
            if abs(ft - pt) > 1e-10:
                return False

    return True


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("Monks et al. (2016) Stroke Pathway DES - Iteration 2")
    print("Step 1: Arrivals (SimPy)  |  Step 2: Testing")
    print("=" * 70)

    sc = Scenario()

    print(f"\nScenario parameters:")
    print(f"  Categories:        {sc.categories}")
    print(f"  Mean IATs (days):  {sc.mean_iat_days}")
    print(f"  Warm-up:           {sc.warm_up_period/365:.0f} years")
    print(f"  Collection period: {sc.results_collection_period/365:.0f} years")
    print(f"  Replications:      {sc.n_reps}")

    test_results = {}

    # --- Test 3: Distribution sampling ---
    print("\n" + "-" * 70)
    print("TEST 3: Exponential distribution class (10,000 samples per IAT)")
    print("-" * 70)
    df_dist = test_exponential_distribution(sc)
    print(df_dist.to_string(index=False))
    test_results["distribution"] = df_dist["PASS"].all()
    print(f">>> {'PASS' if test_results['distribution'] else 'FAIL'}")

    # --- Test 4: Reproducibility ---
    print("\n" + "-" * 70)
    print("TEST 4: Reproducibility (same seed -> same output)")
    print("-" * 70)
    test_results["reproducibility"] = test_reproducibility(sc)
    print(f"Same seed produces identical patients: "
          f"{test_results['reproducibility']}")
    print(f">>> {'PASS' if test_results['reproducibility'] else 'FAIL'}")

    # --- Test 5: Warm-up filtering ---
    print("\n" + "-" * 70)
    print("TEST 5: No arrivals before warm-up in output")
    print("-" * 70)
    test_results["warmup_filter"] = test_no_warm_up_arrivals(sc)
    print(f"All output arrivals after warm-up: "
          f"{test_results['warmup_filter']}")
    print(f">>> {'PASS' if test_results['warmup_filter'] else 'FAIL'}")

    # --- Test 6: Category exclusion ---
    print("\n" + "-" * 70)
    print("TEST 6: Category exclusion (seed stability check)")
    print("-" * 70)
    test_results["category_exclusion"] = test_category_exclusion(sc)
    print(f"Excluding a category preserves other streams: "
          f"{test_results['category_exclusion']}")
    print(f">>> {'PASS' if test_results['category_exclusion'] else 'FAIL'}")

    # --- Run all replications ---
    print("\n" + "-" * 70)
    print(f"Running {sc.n_reps} replications...")
    print("-" * 70)
    results_df = run_replications(sc)

    # --- Test 1: Arrival counts ---
    print("\n" + "-" * 70)
    print("TEST 1: Mean annual arrivals vs theoretical (95% CI check)")
    print("-" * 70)
    df_counts = test_arrival_counts(results_df, sc)
    print(df_counts.to_string(index=False))
    test_results["arrival_counts"] = df_counts["PASS"].all()
    print(f">>> {'PASS' if test_results['arrival_counts'] else 'FAIL'}")

    # --- Test 2: Category proportions ---
    print("\n" + "-" * 70)
    print("TEST 2: Category proportions vs base-period (<3pp tolerance)")
    print("-" * 70)
    df_props = test_arrival_proportions(results_df, sc)
    print(df_props.to_string(index=False))
    test_results["proportions"] = df_props["PASS"].all()
    print(f">>> {'PASS' if test_results['proportions'] else 'FAIL'}")

    # --- Descriptive summary ---
    print("\n" + "-" * 70)
    print("Summary statistics: annual arrival rates across replications")
    print("-" * 70)
    summary_cols = list(sc.categories) + ["total"]
    print(results_df[summary_cols].describe().round(1).to_string())

    # --- Quick demo of category exclusion (Scenario 4) ---
    print("\n" + "-" * 70)
    print("Demo: single replication with complex_neuro excluded")
    print("-" * 70)
    demo_patients = run_single_replication(
        sc, rep_seed=42,
        categories=["stroke", "tia", "other"]
    )
    demo_counts = summarise_arrivals(demo_patients, sc)
    demo_total = sum(demo_counts.values())
    print(f"Total patients (5-year collection): {demo_total}")
    for cat in sc.categories:
        print(f"  {cat:14s}: {demo_counts[cat]:5d}")

    # --- Overall verdict ---
    print("\n" + "=" * 70)
    for name, passed in test_results.items():
        print(f"  {name:25s}: {'PASS' if passed else 'FAIL'}")
    print("-" * 70)
    all_pass = all(test_results.values())
    print(
        f"  OVERALL: "
        f"{'ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED'}"
    )
    print("=" * 70)
