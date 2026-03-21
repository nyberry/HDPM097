# Validation Results

This section summarises the current validation status of the recreated stroke pathway model against the published Monks et al. results.

## Validation approach

The recreation uses the paper's occupancy-audit concept. Daily occupancy is simulated under unfettered demand and then converted into estimated delay probabilities using the Erlang-loss-style occupancy formula described in the paper.

The current validation focuses on the "current admissions" scenario for:

- acute bed delay probabilities
- rehabilitation bed delay probabilities
- qualitative agreement of the acute occupancy distribution
- qualitative agreement of the acute delay trade-off curve

## Key figures

- Acute occupancy distribution: `docs/figures/iteration_03_acute_occupancy_distribution.png`
- Acute delay trade-off curve: `docs/figures/iteration_04_acute_delay_tradeoff.png`

## Interpretation

At the current stage, the recreated model reproduces the published current-admissions delay table closely when delay is estimated using the paper's Erlang-loss-style occupancy calculation rather than a naive threshold probability.

This is encouraging because it suggests that:

- the encoded arrival rates, LOS distributions, and routing tables are broadly coherent
- the occupancy audit model is behaving similarly to the published model in the base scenario
- the main remaining gaps are likely to be in secondary detail rather than the core pathway structure

## Limitations of the current validation

- the current notebook uses a reduced replication count for faster iteration
- the stroke mortality LOS subgroup is not yet modelled explicitly as a separate routing branch
- the validation so far is strongest for the current-admissions scenario rather than the full scenario set in the paper

These limitations should be described explicitly in the final report.
