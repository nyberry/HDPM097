import pandas as pd

from stroke_sim.validation import build_two_scenario_table


def test_two_scenario_table_has_expected_columns() -> None:
    baseline = pd.DataFrame(
        [
            {"beds": 10, "model_p_delay": 0.14},
            {"beds": 11, "model_p_delay": 0.09},
        ]
    )
    scenario = pd.DataFrame(
        [
            {"beds": 10, "model_p_delay": 0.09},
            {"beds": 11, "model_p_delay": 0.05},
        ]
    )
    table = build_two_scenario_table(
        baseline,
        scenario,
        bed_label="No. acute beds",
        baseline_prefix="current",
        scenario_prefix="no_complex",
    )
    assert list(table.columns) == [
        "bed_group",
        "beds",
        "current_p_delay",
        "current_1_in_n",
        "no_complex_p_delay",
        "no_complex_1_in_n",
    ]
