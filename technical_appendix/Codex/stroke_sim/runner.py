"""Entry points for development experiments and validation runs."""

from __future__ import annotations

from dataclasses import asdict

import pandas as pd

from .config import SimulationSettings
from .metrics import erlang_loss_probability_from_audit, occupancy_distribution
from .model import StrokePathwayModel


def run_single_replication(
    *,
    random_seed: int = 42,
    settings: SimulationSettings | None = None,
) -> dict[str, pd.DataFrame | dict[str, int | float]]:
    """Run one occupancy-audit replication and return audit and summary frames."""
    settings = settings or SimulationSettings()
    result = StrokePathwayModel(settings=settings, random_seed=random_seed).run()
    audit = result.daily_audit
    return {
        "audit": audit,
        "acute_distribution": occupancy_distribution(audit, "acute_occupancy"),
        "acute_stroke_distribution": occupancy_distribution(audit, "acute_stroke_occupancy"),
        "rehab_distribution": occupancy_distribution(audit, "rehab_occupancy"),
        "settings": asdict(settings),
    }


def run_replications(
    *,
    settings: SimulationSettings | None = None,
    start_seed: int = 42,
) -> pd.DataFrame:
    """Run multiple replications and return a combined daily audit."""
    settings = settings or SimulationSettings()
    audits: list[pd.DataFrame] = []
    for offset in range(settings.replications):
        result = StrokePathwayModel(settings=settings, random_seed=start_seed + offset).run()
        audit = result.daily_audit.copy()
        audit["replication"] = offset + 1
        audits.append(audit)
    return pd.concat(audits, ignore_index=True)


def build_delay_tradeoff(
    audit: pd.DataFrame,
    *,
    column: str,
    bed_range: range,
) -> pd.DataFrame:
    """Build a trade-off table of beds versus Erlang-style delay probability."""
    rows = []
    for beds in bed_range:
        rows.append(
            {
                "beds": beds,
                "p_delay": erlang_loss_probability_from_audit(audit, column, beds),
            }
        )
    return pd.DataFrame(rows)
