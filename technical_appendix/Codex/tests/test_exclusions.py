from stroke_sim.config import SimulationSettings
from stroke_sim.runner import run_replications


def test_excluding_complex_neurological_reduces_rehab_occupancy() -> None:
    current_audit = run_replications(
        settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2)
    )
    no_complex_audit = run_replications(
        settings=SimulationSettings(
            run_length_days=365,
            warm_up_days=90,
            replications=2,
            excluded_patient_groups=("complex_neurological",),
        )
    )
    assert no_complex_audit["rehab_occupancy"].mean() < current_audit["rehab_occupancy"].mean()
