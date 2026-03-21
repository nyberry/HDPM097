"""Metrics and output calculations for occupancy and delay."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def occupancy_distribution(audit: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return a percentage occupancy distribution for an audited ward column."""
    counts = Counter(int(value) for value in audit[column])
    total = sum(counts.values())
    rows = [
        {
            "occupancy": occupancy,
            "count": count,
            "percent": 100.0 * count / total,
        }
        for occupancy, count in sorted(counts.items())
    ]
    return pd.DataFrame(rows)


def probability_delay_from_audit(audit: pd.DataFrame, column: str, beds: int) -> float:
    """Estimate the probability that occupancy is at or above a bed limit."""
    if audit.empty:
        raise ValueError("audit must not be empty")
    return float((audit[column] >= beds).mean())


def erlang_loss_probability_from_audit(audit: pd.DataFrame, column: str, beds: int) -> float:
    """Estimate delay probability using the paper's Erlang-loss-style occupancy formula."""
    if audit.empty:
        raise ValueError("audit must not be empty")
    counts = Counter(int(value) for value in audit[column])
    total = sum(counts.values())
    p_equal = counts.get(beds, 0) / total
    p_less_equal = sum(count for occupancy, count in counts.items() if occupancy <= beds) / total
    if p_less_equal == 0:
        return 0.0
    return p_equal / p_less_equal


def plot_occupancy_distribution(
    distribution: pd.DataFrame,
    *,
    title: str,
    x_label: str,
    output_path: str | Path | None = None,
    max_x: int | None = None,
) -> plt.Figure:
    """Plot a bar chart resembling the occupancy PDF figure in the paper."""
    if distribution.empty:
        raise ValueError("distribution must not be empty")

    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.bar(distribution["occupancy"], distribution["percent"], width=0.38, color="black", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(x_label, fontweight="bold")
    ax.set_ylabel("% observations", fontweight="bold")
    ax.set_ylim(0, max(16, distribution["percent"].max() * 1.15))
    ax.yaxis.grid(True, color="#d0d0d0", linewidth=1)
    ax.set_axisbelow(True)
    if max_x is not None:
        ax.set_xlim(1, max_x)
        ax.set_xticks(range(1, max_x + 1))
    else:
        max_occ = int(distribution["occupancy"].max())
        ax.set_xticks(range(0, max_occ + 1))
    for spine in ax.spines.values():
        spine.set_linewidth(1)
    fig.tight_layout()
    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=200, bbox_inches="tight")
    return fig


def plot_delay_tradeoff_curve(
    tradeoff: pd.DataFrame,
    *,
    title: str,
    x_label: str,
    output_path: str | Path | None = None,
) -> plt.Figure:
    """Plot a step chart resembling the paper's delay trade-off figure."""
    if tradeoff.empty:
        raise ValueError("tradeoff must not be empty")

    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    ax.step(tradeoff["beds"], tradeoff["p_delay"], where="post", color="black", linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(x_label, fontweight="bold")
    ax.set_ylabel("Probability of delay", fontweight="bold")
    ax.set_ylim(0, 1.0)
    ax.set_xlim(0, max(tradeoff["beds"]) + 1)
    ax.yaxis.grid(True, color="#d0d0d0", linewidth=1)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_linewidth(1)
    fig.tight_layout()
    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=200, bbox_inches="tight")
    return fig
