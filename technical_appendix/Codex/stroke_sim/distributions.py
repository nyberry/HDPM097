"""Distribution helpers for the stroke pathway model."""

from __future__ import annotations

import math


def lognormal_mu_sigma_from_mean_sd(mean: float, sd: float) -> tuple[float, float]:
    """Convert arithmetic mean and standard deviation to lognormal parameters."""
    if mean <= 0:
        raise ValueError("mean must be positive")
    if sd <= 0:
        raise ValueError("sd must be positive")

    variance = sd ** 2
    sigma2 = math.log(1 + variance / (mean ** 2))
    mu = math.log(mean) - 0.5 * sigma2
    sigma = math.sqrt(sigma2)
    return mu, sigma
