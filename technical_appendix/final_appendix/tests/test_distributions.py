from stroke_sim.distributions import lognormal_mu_sigma_from_mean_sd


def test_lognormal_parameter_conversion_returns_positive_sigma() -> None:
    mu, sigma = lognormal_mu_sigma_from_mean_sd(7.4, 8.6)
    assert isinstance(mu, float)
    assert sigma > 0


