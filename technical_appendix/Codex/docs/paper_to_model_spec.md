# Paper To Model Specification

## Purpose

This document translates the assignment brief and Monks et al. paper into an implementable specification for a Python/SimPy recreation.

## Assignment framing

The assignment is not only to build a simulation, but to conduct a research study on whether a published healthcare DES can be recreated from natural-language documentation. The technical appendix must therefore preserve:

- the sequence of iterations
- prompts given to any LLM
- generated and revised code
- tests and tester notes
- runnable notebooks and environment details

## Recommended recreation target

Primary target:

- Recreate the Monks et al. base stroke pathway model closely enough to produce similar occupancy and delay results for the published scenarios.

Secondary target:

- Keep the implementation simple enough to be understandable by a data scientist and explain where simplifications are made.

## System boundary

The model represents the stroke pathway from admission to:

- acute stroke unit
- inpatient rehabilitation ward
- early supported discharge (ESD)
- other destinations

The paper focuses on bed capacity planning in the acute and rehabilitation wards. ESD is included as a routing destination but does not itself appear to require explicit bed-capacity modelling in the published results.

## Entities

Patient groups named in the paper:

- Stroke
- TIA
- Complex-neurological
- Other

Stroke patients are further split by downstream pathway attributes:

- ESD eligible
- non-ESD
- mortality subgroup in acute LOS table

## Arrivals

From the paper:

- new admissions are modelled with exponential inter-arrival times
- each patient group has its own arrival process

Implementation implication:

- represent each patient group as an independent Poisson arrival stream
- parameterise arrival rates using mean inter-arrival times from the paper and figures/tables

Base scenario arrival rates from Figure 2:

- Acute admission to acute stroke unit:
  - Stroke: every 1.2 days
  - TIA: every 9.3 days
  - Complex-neurological: every 3.6 days
  - Other: every 3.2 days
- Transfer from elsewhere to rehab:
  - Stroke: every 21.8 days
  - TIA: not applicable
  - Complex-neurological: every 31.7 days
  - Other: every 28.6 days

## Service / length of stay

From the appendix:

- acute LOS uses lognormal distributions
- rehabilitation LOS uses lognormal distributions
- LOS depends on patient subgroup and destination characteristics

Implementation implication:

- store LOS parameters by ward and subgroup
- convert reported mean and standard deviation into lognormal sampling parameters
- validate sampled means and percentiles against reported summaries

Base LOS families encoded for the base scenario:

- Acute:
  - stroke_no_esd
  - stroke_esd
  - stroke_mortality
  - tia
  - complex_neurological
  - other
- Rehab:
  - stroke_no_esd
  - stroke_esd
  - tia
  - complex_neurological
  - other

## Routing

From the appendix:

- acute unit to rehab / ESD / other transfer matrix is given
- rehab unit to ESD / other transfer matrix is given

Implementation implication:

- route patients probabilistically on discharge from each stage
- document any handling of mortality and bounce-back behaviour if simplified

Note:

- the rehab routing percentages for `other` sum to 101% in the appendix, which appears to be a rounding issue in the published table and should be preserved as a documented ambiguity

## Capacity and delay logic

The original paper models "unfettered" demand and estimates delay probability from occupancy distributions rather than directly blocking patients inside a constrained bed model.

Implication for recreation:

- preferred faithful approach: simulate demand for occupancy over time, derive occupancy distribution, then compute `p(delay)` for specified bed counts
- fallback simplified approach: use explicit SimPy capacity constraints and observe blocking events directly

Current recommendation:

- implement the faithful occupancy-driven approach first for the base scenario
- use explicit-capacity simulation only if needed for comparison or simplification

## Main outputs to reproduce

- occupancy summaries and occupancy distributions
- probability of delay `p(delay)` for acute and rehab beds
- "1 in every n patients delayed"
- scenario comparison tables
- trade-off curves between bed numbers and delay probability
- average occupancy comparison discussed in the paper

## Scenarios explicitly identified in the paper

- current admissions
- 5% more admissions
- pooling of acute and rehab beds
- partial pooling of acute and rehab beds
- no complex-neurological patients
- ring-fenced stroke beds

## Simulation execution details

From the paper:

- run length: 5 years
- warm-up: 3 years
- replications: 150

Implementation implication:

- preserve these as defaults for validation runs
- use smaller runs during development tests

## Validation strategy

Model development should validate in layers:

1. Input validation
   - arrival rates match target means
   - LOS sampling matches target summaries
   - routing proportions match transfer matrices
2. Mechanics validation
   - occupancy audit is recorded correctly
   - warm-up removal is handled correctly
3. Output validation
   - base scenario delay tables are approximately reproduced
   - scenario comparisons have the same qualitative patterns as the paper

## Initial implementation scope

Iteration 01 should focus on:

- project scaffold
- parameter registry
- lognormal conversion utilities
- patient group definitions
- paper-to-model extraction
- explicit list of assumptions and ambiguities

Iteration 02 can then focus on:

- independent arrival streams
- unconstrained occupancy accounting for acute and rehab
- daily occupancy audit
