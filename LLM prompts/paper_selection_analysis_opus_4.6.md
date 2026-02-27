# Paper Selection Analysis — HPDM097 Coursework 2

## Overview

This document records the group's analysis of the four suggested papers for the DES model recreation assignment using Clause Opus 4.6 . The goal was to select a paper with an appropriate level of complexity, sufficient data reporting, and feasibility for recreation in Python/SimPy.

The four candidate papers are:

1.  **Penn et al. (2019)** — *Towards generic modelling of hospital wards: Reuse and redevelopment of simple models*
2.  **Lahr et al. (2013)** — *A Simulation-based Approach for Improving Utilization of Thrombolysis in Acute Brain Infarction*
3.  **Griffiths et al. (2010)** — *A simulation model of bed-occupancy in a critical care unit*
4.  **Monks et al. (2016)** — *A modelling tool for capacity planning in acute and community stroke services*

------------------------------------------------------------------------

## Evaluation Criteria

Each paper was assessed against the following criteria:

-   **Model structure** — How clearly is the model logic described? Is there a flow diagram?
-   **Data completeness** — Are distribution types and parameters fully reported?
-   **SimPy feasibility** — How naturally does the model map to SimPy constructs (Resources, queues, processes)?
-   **Validation opportunity** — Are there reported outputs to validate a recreation against?
-   **Simplification scope** — Can the model be reasonably simplified while meeting the assignment's minimum complexity requirement?

------------------------------------------------------------------------

## Paper-by-Paper Analysis

### 1. Griffiths et al. (2010) — CCU Bed-Occupancy

**Model structure:** A single Critical Care Unit (24 funded beds, 5 additional unfunded) with six arrival sources: A&E, Ward, Emergency Surgery, Other Hospital, X-Ray, and Elective Surgery. Patients are classified as planned (Elective) or unplanned. Elective patients who find no beds have their surgery cancelled; unplanned patients queue until a bed is available. A clear flow diagram (Figure 1) is provided.

**Data completeness:**

| Component | Detail provided | Notes |
|----|----|----|
| Inter-arrival times (5 sources) | Negative Exponential — means fully reported | e.g. A&E = 22.72 hrs, Ward = 26.0 hrs |
| Inter-arrival times (Elective) | Normal distribution for arrival hour (mean 17.91, SD 3.16) | Time-dependent; more complex to implement |
| Length of stay (3 sources) | Hyperexponential (3–4 stage) — mean and SD only | Phase parameters not reported |
| Length of stay (2 sources) | Lognormal — fully parameterised | Other Hospital and X-Ray |
| Length of stay (Elective) | Sampled from empirical data | Data not available |
| Bed changeover time | 5 hours assumed | Sensitivity analysis reported (2–8 hrs) |
| Validation targets | 57 cancellations/year, 82% occupancy at 24 beds | Table 2 gives results for 22–29 beds |

**Key challenge:** Three of the six length-of-stay distributions are Hyperexponential with only aggregate statistics reported (mean and SD), not the individual phase parameters needed to sample from the distribution. This would need to be addressed through a justified simplification, such as substituting Lognormal distributions fitted to the reported mean and SD. The Elective arrival process is also time-dependent, adding implementation complexity.

**SimPy feasibility:** The model maps well to SimPy: a `Resource(capacity=N)` for beds, separate arrival generators per source, and priority-based queuing (unplanned wait, planned are cancelled). This is a classical DES structure.

**Validation opportunity:** Strong. Table 2 provides occupancy and cancellation counts across a range of bed numbers (22–29), enabling multi-scenario validation.

**Simplification options:** - Replace Hyperexponential LoS distributions with Lognormal fitted to reported mean/SD. - Sample Elective LoS from a fitted distribution rather than empirical data. - Simplify Elective arrival scheduling (e.g. fixed daily schedule rather than time-dependent Normal). - Reduce the number of arrival sources (e.g. combine A&E, Ward, and Emergency into a single "unplanned" stream).

------------------------------------------------------------------------

### 2. Penn et al. (2019) — Generic Hospital Ward Model

**Model structure:** Two models are reported. The **archetype ward model** handles patient arrivals, gender assignment, and bed allocation into a configurable mix of single rooms and multi-bed bays. A 5-step gender-aware bay assignment algorithm governs placement. The **ICU adaptation** removes gender separation but adds care-level routing and transfer/cancellation logic.

**Data completeness:**

| Component | Detail provided | Notes |
|----|----|----|
| Arrival distributions | Empirical distributions | No parametric form; raw data entered via Excel |
| Length of stay distributions | Empirical distributions | As above |
| Ward configuration | Configurable (bays + singles) | Example: 50-bed ward with varying bay/single splits |
| Sample results | Table 2: occupancy, wait, transfers | For the community rehab ward application |
| Model files | Available on Zenodo (DOI 10.5281/zenodo.1468287) | Simul8 + Excel format |

**Key challenge:** The bay allocation algorithm is the most complex logic across all four papers — five steps involving gender-matching, bay switching, and patient transfers between beds. Without it, the model loses its distinguishing feature. The reliance on empirical distributions without parametric forms means distribution parameters would need to be extracted from the Zenodo data files or synthetic data generated.

**SimPy feasibility:** The basic flow (queue → decision → ward → discharge) is straightforward. However, implementing the gender-aware bay allocation algorithm in SimPy requires careful tracking of bay occupancy by gender, which adds significant coding effort.

**Validation opportunity:** Moderate. Sample results are given for the rehab ward application, but these depend on the specific empirical data used.

**Simplification options:** - Remove gender separation (the paper notes this is possible by treating all patients as one gender), but this removes the core complexity. - Focus on the ICU model instead, which does not require gender logic. - Use parametric distributions fitted to the Zenodo data.

------------------------------------------------------------------------

### 3. Lahr et al. (2013) — Acute Stroke Thrombolysis

**Model structure:** A process-flow model of the acute stroke pathway from symptom onset to tPA treatment decision. Three patient routes (EMS transport, self-transport, in-hospital stroke) branch through pre-hospital and intra-hospital activities: call for help, first responder, EMS response/on-scene/transport, neurological exam, neuroimaging, lab evaluation, treatment decision, and tPA mixing.

**Data completeness:**

| Component | Detail provided | Notes |
|----|----|----|
| Activity durations | Mean and 95% CI for all activities | Table 1 in paper; online appendix has further detail |
| Routing probabilities | Fully reported | e.g. 76% EMS, 21% self-transport, 3% in-hospital |
| Diagnostic accuracy | Reported | Treatment eligibility criteria included |
| Validation targets | tPA rate 21.8%, OTT 129 min | Compared against real-system values |

**Key challenge:** This model has **no queuing and no resource constraints**. It is essentially a process-timing/Monte Carlo model — patients flow through a series of timed activities and the simulation evaluates whether accumulated time falls within treatment windows. It uses 10,000 fixed patient journeys rather than replications with warm-up. While it can be built in SimPy, it would barely exercise SimPy's core features (Resources, queuing, capacity). The assignment brief explicitly notes this non-typical approach.

**SimPy feasibility:** Technically implementable but does not leverage SimPy's strengths. No `Resource` objects or queue management needed. More naturally suited to a simple Monte Carlo approach.

**Validation opportunity:** Good — tPA treatment rates and OTT distributions are reported for baseline and scenarios.

**Simplification options:** Limited scope for simplification since the model is already a process-flow without queuing. Could reduce the number of routing branches.

------------------------------------------------------------------------

### 4. Monks et al. (2016) — Stroke Capacity Planning

**Model structure:** Four patient types (Stroke, TIA, Complex Neurological, Other) arrive at an acute stroke unit and flow to a rehabilitation unit or Early Supported Discharge (ESD). The model is intentionally **unconstrained** — there are no bed limits. Patients flow freely, and the resulting occupancy distribution is used with the Erlang loss formula to analytically compute the probability of delay for any given number of beds. A clear model diagram (Figure 2) and occupancy distribution (Figure 1) are provided.

**Data completeness:**

| Component | Detail provided | Notes |
|----|----|----|
| Inter-arrival times | Exponential — means given in paper and Figure 2 | Stroke: 1.2 days, TIA: 9.3 days, Complex Neuro: 3.6 days, Other: 3.2 days |
| Acute LoS | Lognormal — full parameters in supplementary appendix | Mean, SD, median, and percentiles for all 6 subcategories |
| Rehab LoS | Lognormal — full parameters in supplementary appendix | As above |
| Routing probabilities | Implied by model diagram | ESD eligibility percentages derivable from patient counts |
| Run settings | 5-year run, 3-year warm-up, 150 replications | Clearly specified |
| Validation | p(delay) curves and occupancy distributions | Figures 1 and 3; results tables in appendix |

**Key challenge:** The model's unconstrained design means there are no queues in the traditional SimPy sense — occupancy is tracked but never capped. The analytical p(delay) calculation via Erlang loss sits outside the simulation. A group could alternatively implement a constrained version (with actual bed resources and queuing), which would deviate from the paper but create a more conventional DES — and this design choice could be discussed in the report.

**SimPy feasibility:** Very high for the acute-only simplification. Standard exponential arrivals and lognormal LoS are straightforward. If implemented with constraints, the model uses SimPy Resources naturally. If unconstrained, it is simpler but less representative of typical DES modelling.

**Validation opportunity:** Strong. The p(delay) trade-off curve (Figure 3) and occupancy distributions provide clear validation targets. The appendix contains additional results tables.

**Simplification options:** - Focus on the acute stroke unit only (removing rehab and ESD), as suggested by the assignment brief. - Simplify to fewer patient types (e.g. Stroke only, or Stroke + Other). - Implement as a constrained model with explicit bed resources.

------------------------------------------------------------------------

## Comparative Summary

| Criterion | Griffiths et al. | Penn et al. | Lahr et al. | Monks et al. |
|----|----|----|----|----|
| Flow diagram clarity | ✅ Clear (Fig. 1) | ✅ Clear (Fig. 1 & 2) | ✅ Clear (Fig. 1) | ✅ Clear (Fig. 2) |
| Distribution parameters reported | ⚠️ Partial (Hyperexp. phases missing) | ❌ Empirical only | ✅ Full (means + CIs) | ✅ Full (Lognormal params in appendix) |
| Queuing / resource competition | ✅ Yes — beds as shared resource | ✅ Yes — beds + bay logic | ❌ No queuing | ⚠️ By design unconstrained; can be added |
| Validation targets | ✅ Excellent (multi-scenario) | ⚠️ Moderate | ✅ Good | ✅ Good (p(delay) curves) |
| Coding complexity | Medium | High (bay algorithm) | Low (but non-standard) | Low–Medium |
| Simplification scope | Good | Good but loses core feature | Limited | Excellent (acute-only) |
| Exercises core DES concepts | ✅ Strongly | ✅ Strongly | ❌ Weakly | ⚠️ Depends on implementation choice |

------------------------------------------------------------------------

## Recommendation

**Top choices: Griffiths et al. (2010) or Monks et al. (2016)**

Both offer well-described models with clear flow diagrams and sufficient data for recreation. The choice depends on the group's priorities:

-   **Monks et al.** offers the **smoothest implementation path**: all parameters are fully reported as Lognormal distributions, the supplementary appendix is available, and the acute-only simplification is clean and well-justified. The main discussion point for the report is the constrained vs. unconstrained design choice.

-   **Griffiths et al.** offers a **more classical DES structure** with queuing, priority handling, and resource competition — all core concepts in discrete-event simulation. The incomplete distribution reporting (Hyperexponential phases) provides a natural and well-justified simplification to document. Validation targets are excellent.

**Not recommended:**

-   **Lahr et al.** — The absence of queuing and resource constraints limits the opportunity to demonstrate DES modelling competence.
-   **Penn et al.** — The bay allocation algorithm adds substantial coding complexity with limited payoff within a 2000-word report, and the lack of parametric distributions creates an additional barrier.

------------------------------------------------------------------------

*Analysis conducted with assistance from Claude (Anthropic) as part of the paper selection process. This conversation is documented as part of the group's evidence of working.*
