import pandas as pd

from stroke_sim.validation import build_table_2_style


def test_table_2_style_layout_has_expected_columns() -> None:
    current = pd.DataFrame(
        [
            {"beds": 10, "model_p_delay": 0.14},
            {"beds": 11, "model_p_delay": 0.09},
        ]
    )
    more = pd.DataFrame(
        [
            {"beds": 10, "model_p_delay": 0.16},
            {"beds": 11, "model_p_delay": 0.11},
        ]
    )
    table = build_table_2_style(current, more, bed_label="No. acute beds")
    assert list(table.columns) == [
        "bed_group",
        "beds",
        "current_p_delay",
        "current_1_in_n",
        "more_p_delay",
        "more_1_in_n",
    ]
