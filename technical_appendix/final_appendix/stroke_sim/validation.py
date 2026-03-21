"""Published comparison targets and validation helpers."""

from __future__ import annotations

import pandas as pd

from .metrics import erlang_loss_probability_from_audit


PUBLISHED_CURRENT_ADMISSIONS_ACUTE = pd.DataFrame(
    [
        {"beds": 9, "published_p_delay": 0.19},
        {"beds": 10, "published_p_delay": 0.14},
        {"beds": 11, "published_p_delay": 0.09},
        {"beds": 12, "published_p_delay": 0.06},
        {"beds": 13, "published_p_delay": 0.04},
        {"beds": 14, "published_p_delay": 0.02},
    ]
)


PUBLISHED_CURRENT_ADMISSIONS_ACUTE_10_TO_15 = pd.DataFrame(
    [
        {"beds": 10, "published_p_delay": 0.14},
        {"beds": 11, "published_p_delay": 0.09},
        {"beds": 12, "published_p_delay": 0.06},
        {"beds": 13, "published_p_delay": 0.04},
        {"beds": 14, "published_p_delay": 0.02},
        {"beds": 15, "published_p_delay": 0.01},
    ]
)


PUBLISHED_CURRENT_ADMISSIONS_REHAB = pd.DataFrame(
    [
        {"beds": 10, "published_p_delay": 0.20},
        {"beds": 12, "published_p_delay": 0.11},
        {"beds": 13, "published_p_delay": 0.08},
        {"beds": 14, "published_p_delay": 0.05},
        {"beds": 15, "published_p_delay": 0.03},
        {"beds": 16, "published_p_delay": 0.02},
    ]
)


PUBLISHED_MORE_ADMISSIONS_ACUTE = pd.DataFrame(
    [
        {"beds": 10, "published_p_delay": 0.16},
        {"beds": 11, "published_p_delay": 0.11},
        {"beds": 12, "published_p_delay": 0.07},
        {"beds": 13, "published_p_delay": 0.05},
        {"beds": 14, "published_p_delay": 0.03},
    ]
)


PUBLISHED_MORE_ADMISSIONS_REHAB = pd.DataFrame(
    [
        {"beds": 12, "published_p_delay": 0.13},
        {"beds": 13, "published_p_delay": 0.09},
        {"beds": 14, "published_p_delay": 0.07},
        {"beds": 15, "published_p_delay": 0.04},
        {"beds": 16, "published_p_delay": 0.02},
    ]
)


PUBLISHED_NO_COMPLEX_ACUTE = pd.DataFrame(
    [
        {"beds": 10, "published_p_delay": 0.09},
        {"beds": 11, "published_p_delay": 0.05},
        {"beds": 12, "published_p_delay": 0.03},
        {"beds": 13, "published_p_delay": 0.02},
        {"beds": 14, "published_p_delay": 0.01},
        {"beds": 15, "published_p_delay": 0.01},
    ]
)


PUBLISHED_NO_COMPLEX_REHAB = pd.DataFrame(
    [
        {"beds": 12, "published_p_delay": 0.03},
        {"beds": 13, "published_p_delay": 0.02},
        {"beds": 14, "published_p_delay": 0.01},
        {"beds": 15, "published_p_delay": 0.01},
        {"beds": 16, "published_p_delay": 0.00},
    ]
)


PUBLISHED_RING_FENCED_ACUTE = pd.DataFrame(
    [
        {"beds": 10, "published_p_delay": 0.08},
        {"beds": 11, "published_p_delay": 0.05},
        {"beds": 12, "published_p_delay": 0.03},
        {"beds": 13, "published_p_delay": 0.02},
        {"beds": 14, "published_p_delay": 0.01},
        {"beds": 15, "published_p_delay": 0.00},
    ]
)


def compare_to_published_table(audit: pd.DataFrame, *, column: str, published: pd.DataFrame) -> pd.DataFrame:
    """Compare audited Erlang-style delay estimates to a published table."""
    rows = []
    for row in published.to_dict(orient="records"):
        beds = int(row["beds"])
        modelled = erlang_loss_probability_from_audit(audit, column, beds)
        rows.append(
            {
                "beds": beds,
                "published_p_delay": row["published_p_delay"],
                "model_p_delay": modelled,
                "abs_error": abs(modelled - row["published_p_delay"]),
            }
        )
    return pd.DataFrame(rows)


def build_report_table(comparison: pd.DataFrame) -> pd.DataFrame:
    """Create a report-friendly side-by-side validation table."""
    report = comparison.copy()
    report["recreated_p_delay"] = report["model_p_delay"].round(3)
    report["published_p_delay"] = report["published_p_delay"].round(3)
    report["abs_error"] = report["abs_error"].round(3)
    report["published_1_in_n"] = report["published_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    report["recreated_1_in_n"] = report["recreated_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    return report[
        [
            "beds",
            "published_p_delay",
            "recreated_p_delay",
            "abs_error",
            "published_1_in_n",
            "recreated_1_in_n",
        ]
    ]


def build_table_2_style(
    current_comparison: pd.DataFrame,
    more_comparison: pd.DataFrame,
    *,
    bed_label: str,
    include_only_more_beds: set[int] | None = None,
) -> pd.DataFrame:
    """Build a table shaped like Monks et al. Table 2."""
    current = current_comparison.copy()
    current["current_p_delay"] = current["model_p_delay"].round(2)
    current["current_1_in_n"] = current["current_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    current = current[["beds", "current_p_delay", "current_1_in_n"]]

    more = more_comparison.copy()
    more["more_p_delay"] = more["model_p_delay"].round(2)
    more["more_1_in_n"] = more["more_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    more = more[["beds", "more_p_delay", "more_1_in_n"]]

    table = current.merge(more, on="beds", how="left")
    if include_only_more_beds is not None:
        for column in ["more_p_delay", "more_1_in_n"]:
            table.loc[~table["beds"].isin(include_only_more_beds), column] = None
    table.insert(0, "bed_group", "")
    if not table.empty:
        table.loc[0, "bed_group"] = bed_label
    return table


def build_two_scenario_table(
    baseline_comparison: pd.DataFrame,
    scenario_comparison: pd.DataFrame,
    *,
    bed_label: str,
    baseline_prefix: str,
    scenario_prefix: str,
) -> pd.DataFrame:
    """Build a two-scenario comparison table with paired delay columns."""
    baseline = baseline_comparison.copy()
    baseline["_raw_model_p_delay"] = baseline["model_p_delay"]
    baseline[f"{baseline_prefix}_p_delay"] = baseline["model_p_delay"].round(2)
    baseline[f"{baseline_prefix}_1_in_n"] = baseline["_raw_model_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    baseline = baseline[["beds", f"{baseline_prefix}_p_delay", f"{baseline_prefix}_1_in_n"]]

    scenario = scenario_comparison.copy()
    scenario["_raw_model_p_delay"] = scenario["model_p_delay"]
    scenario[f"{scenario_prefix}_p_delay"] = scenario["model_p_delay"].round(2)
    scenario[f"{scenario_prefix}_1_in_n"] = scenario["_raw_model_p_delay"].apply(
        lambda value: int(round(1 / value)) if value > 0 else None
    )
    scenario = scenario[["beds", f"{scenario_prefix}_p_delay", f"{scenario_prefix}_1_in_n"]]

    table = baseline.merge(scenario, on="beds", how="left")
    table.insert(0, "bed_group", "")
    if not table.empty:
        table.loc[0, "bed_group"] = bed_label
    return table
