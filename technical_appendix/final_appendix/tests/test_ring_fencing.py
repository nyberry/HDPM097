from stroke_sim.config import SimulationSettings
from stroke_sim.metrics import erlang_loss_probability_from_audit
from stroke_sim.runner import run_replications


def test_ring_fenced_stroke_delay_is_lower_than_total_acute_delay() -> None:
    audit = run_replications(settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2))
    total_delay = erlang_loss_probability_from_audit(audit, "acute_occupancy", 10)
    ring_fenced_delay = erlang_loss_probability_from_audit(audit, "acute_stroke_occupancy", 10)
    assert ring_fenced_delay < total_delay
