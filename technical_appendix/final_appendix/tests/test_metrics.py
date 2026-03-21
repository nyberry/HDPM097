from stroke_sim.metrics import occupancy_distribution, probability_delay_from_audit
from stroke_sim.runner import run_single_replication


def test_occupancy_distribution_percentages_sum_to_100() -> None:
    outputs = run_single_replication()
    distribution = occupancy_distribution(outputs["audit"], "acute_occupancy")
    assert round(distribution["percent"].sum(), 8) == 100.0


def test_probability_delay_returns_probability() -> None:
    outputs = run_single_replication()
    probability = probability_delay_from_audit(outputs["audit"], "acute_occupancy", beds=10)
    assert 0.0 <= probability <= 1.0
