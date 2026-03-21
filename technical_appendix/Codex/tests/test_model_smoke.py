from stroke_sim.config import SimulationSettings
from stroke_sim.model import StrokePathwayModel


def test_model_smoke_run_returns_audit_rows() -> None:
    model = StrokePathwayModel(settings=SimulationSettings(run_length_days=30, warm_up_days=10))
    result = model.run()
    assert not result.daily_audit.empty
    assert set(result.daily_audit.columns) == {"day", "acute_occupancy", "acute_stroke_occupancy", "rehab_occupancy"}
