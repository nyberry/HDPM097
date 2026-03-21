from stroke_sim.config import SimulationSettings
from stroke_sim.runner import run_replications


def test_more_admissions_increases_mean_acute_occupancy() -> None:
    current_audit = run_replications(
        settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2, arrival_rate_multiplier=1.0)
    )
    more_audit = run_replications(
        settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2, arrival_rate_multiplier=1.05)
    )
    assert more_audit["acute_occupancy"].mean() > current_audit["acute_occupancy"].mean()
