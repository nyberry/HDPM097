"""Pooling calculations based on audited acute and rehab occupancies."""

from __future__ import annotations

from collections import Counter

import pandas as pd

from .metrics import erlang_loss_probability_from_audit


def _counter(values: pd.Series) -> Counter[int]:
    return Counter(int(value) for value in values)


def _p_equal(counter: Counter[int], n: int, total: int) -> float:
    return counter.get(n, 0) / total


def _p_greater_equal(counter: Counter[int], n: int, total: int) -> float:
    return sum(count for occupancy, count in counter.items() if occupancy >= n) / total


def pooled_delay_probability(audit: pd.DataFrame, *, total_beds: int) -> float:
    """Delay probability when all acute and rehab beds are completely pooled."""
    total_occupancy = audit["acute_occupancy"] + audit["rehab_occupancy"]
    total_audit = pd.DataFrame({"total_occupancy": total_occupancy})
    return erlang_loss_probability_from_audit(total_audit, "total_occupancy", total_beds)


def partial_pooling_delay_probabilities(
    audit: pd.DataFrame,
    *,
    dedicated_acute_beds: int,
    dedicated_rehab_beds: int,
    pooled_beds: int,
) -> tuple[float, float]:
    """Approximate acute and rehab delay probabilities under partial pooling.

    This follows the appendix logic using an independence approximation for the
    acute and rehab occupancy distributions.
    """
    if pooled_beds == 0:
        acute = erlang_loss_probability_from_audit(audit, "acute_occupancy", dedicated_acute_beds)
        rehab = erlang_loss_probability_from_audit(audit, "rehab_occupancy", dedicated_rehab_beds)
        return acute, rehab

    acute_counter = _counter(audit["acute_occupancy"])
    rehab_counter = _counter(audit["rehab_occupancy"])
    acute_total = sum(acute_counter.values())
    rehab_total = sum(rehab_counter.values())

    acute_delay = _p_greater_equal(acute_counter, dedicated_acute_beds + pooled_beds, acute_total)
    for j in range(1, pooled_beds + 1):
        acute_delay += _p_equal(acute_counter, dedicated_acute_beds + pooled_beds - j, acute_total) * _p_greater_equal(
            rehab_counter, dedicated_rehab_beds + j, rehab_total
        )

    rehab_delay = _p_greater_equal(rehab_counter, dedicated_rehab_beds + pooled_beds, rehab_total)
    for j in range(1, pooled_beds + 1):
        rehab_delay += _p_equal(rehab_counter, dedicated_rehab_beds + pooled_beds - j, rehab_total) * _p_greater_equal(
            acute_counter, dedicated_acute_beds + j, acute_total
        )

    return acute_delay, rehab_delay


def build_pooling_results_table(audit: pd.DataFrame) -> pd.DataFrame:
    """Build a Table 3 style pooling results table from audited occupancies."""
    scenarios = [
        {"dedicated_acute": 0, "dedicated_rehab": 0, "pooled": 22, "mode": "complete"},
        {"dedicated_acute": 0, "dedicated_rehab": 0, "pooled": 26, "mode": "complete"},
        {"dedicated_acute": 14, "dedicated_rehab": 12, "pooled": 0, "mode": "partial"},
        {"dedicated_acute": 11, "dedicated_rehab": 11, "pooled": 4, "mode": "partial"},
        {"dedicated_acute": 11, "dedicated_rehab": 10, "pooled": 5, "mode": "partial"},
        {"dedicated_acute": 10, "dedicated_rehab": 10, "pooled": 6, "mode": "partial"},
        {"dedicated_acute": 10, "dedicated_rehab": 9, "pooled": 7, "mode": "partial"},
        {"dedicated_acute": 9, "dedicated_rehab": 9, "pooled": 8, "mode": "partial"},
        {"dedicated_acute": 9, "dedicated_rehab": 8, "pooled": 9, "mode": "partial"},
    ]
    rows = []
    for scenario in scenarios:
        if scenario["mode"] == "complete":
            acute_delay = pooled_delay_probability(audit, total_beds=scenario["pooled"])
            rehab_delay = acute_delay
        else:
            acute_delay, rehab_delay = partial_pooling_delay_probabilities(
                audit,
                dedicated_acute_beds=scenario["dedicated_acute"],
                dedicated_rehab_beds=scenario["dedicated_rehab"],
                pooled_beds=scenario["pooled"],
            )
        rows.append(
            {
                "dedicated_acute": scenario["dedicated_acute"],
                "dedicated_rehab": scenario["dedicated_rehab"],
                "pooled": scenario["pooled"],
                "acute_p_delay": round(acute_delay, 3),
                "rehab_p_delay": round(rehab_delay, 3),
                "acute_1_in_n": int(round(1 / acute_delay)) if acute_delay > 0 else None,
                "rehab_1_in_n": int(round(1 / rehab_delay)) if rehab_delay > 0 else None,
            }
        )
    return pd.DataFrame(rows)
