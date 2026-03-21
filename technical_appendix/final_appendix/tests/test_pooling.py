from stroke_sim.config import SimulationSettings
from stroke_sim.pooling import build_pooling_results_table
from stroke_sim.runner import run_replications


def test_pooling_table_has_expected_columns() -> None:
    audit = run_replications(settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2))
    table = build_pooling_results_table(audit)
    assert list(table.columns) == [
        "dedicated_acute",
        "dedicated_rehab",
        "pooled",
        "acute_p_delay",
        "rehab_p_delay",
        "acute_1_in_n",
        "rehab_1_in_n",
    ]


def test_complete_pooling_26_is_better_than_complete_pooling_22() -> None:
    audit = run_replications(settings=SimulationSettings(run_length_days=365, warm_up_days=90, replications=2))
    table = build_pooling_results_table(audit)
    pooled_22 = table.loc[table["pooled"] == 22, "acute_p_delay"].iloc[0]
    pooled_26 = table.loc[table["pooled"] == 26, "acute_p_delay"].iloc[0]
    assert pooled_26 < pooled_22
