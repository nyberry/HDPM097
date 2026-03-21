from stroke_sim.config import SimulationSettings
from stroke_sim.runner import run_replications
from stroke_sim.validation import (
    PUBLISHED_CURRENT_ADMISSIONS_ACUTE,
    compare_to_published_table,
)


def test_published_comparison_table_has_expected_columns() -> None:
    settings = SimulationSettings(run_length_days=365, warm_up_days=90, replications=2)
    audit = run_replications(settings=settings)
    comparison = compare_to_published_table(
        audit,
        column="acute_occupancy",
        published=PUBLISHED_CURRENT_ADMISSIONS_ACUTE.head(2),
    )
    assert list(comparison.columns) == ["beds", "published_p_delay", "model_p_delay", "abs_error"]
    assert len(comparison) == 2
