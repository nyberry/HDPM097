# Example structure for a DES Replication report

source ChatGPT 5.2

---


For **DES replication projects**, markers tend to reward **clear modelling logic, transparency, and reproducibility** even more than technical complexity.

Below is a **“gold-standard” structure** that aligns very closely with what DES research papers look like. If you follow something like this, your report will read like a **mini academic simulation paper**, which is exactly what the assignment brief is pushing you toward.

---

# Gold-Standard Structure for a DES Replication Report

## 1. Abstract

*(Write this last — ~150 words)*

Include four things only:

* What model you attempted to reproduce
* How you implemented it (Python + SimPy)
* Whether you successfully reproduced the results
* What insights you gained about reproducibility

Example structure:

> This study attempted to recreate the stroke thrombolysis pathway model described in Lahr et al. (2013) using Python and the SimPy discrete event simulation framework. An iterative modelling approach was used, beginning with patient arrivals and progressively implementing pathway activities and treatment decisions. Model outputs were compared with results reported in the original publication. The recreated model produced similar estimates for treatment rates and time-to-treatment, although several modelling assumptions required interpretation due to incomplete reporting in the original paper. The study highlights both the feasibility and challenges of reproducing healthcare simulation models from published descriptions.

---

# 2. Introduction

### Aim

Explain **why simulation is useful in healthcare systems**.

Example themes:

* Complex patient pathways
* Resource constraints
* Evaluating policy changes safely
* DES commonly used for hospital flow

### Context

Introduce the selected paper.

Explain briefly:

* What the original model studied
* Why it matters (stroke treatment time critical)

### Objective

End the introduction with a **clear aim statement**:

> The aim of this project was to recreate the simulation model described in Lahr et al. (2013) using Python and SimPy, and to evaluate whether the results reported in the original study could be reproduced.

---

# 3. Methods

This is the **most important section**.

Break it into subsections.

---

## 3.1 Overview of the Original Model

Explain the system in plain language:

Example:

* Stroke patient suspected
* EMS transport
* Emergency department assessment
* Imaging
* Treatment decision
* Thrombolysis if eligible

Include your **flow diagram here**.

Example caption:

> **Figure 1:** Simplified process flow for the stroke thrombolysis pathway based on Lahr et al. (2013).

---

## 3.2 Model Assumptions

Papers rarely describe everything clearly.

You must **explicitly state assumptions**.

Example table:

| Component            | Assumption                |
| -------------------- | ------------------------- |
| Patient arrivals     | Poisson process           |
| Activity times       | Lognormal distributions   |
| Resource constraints | Not modelled              |
| Eligibility          | Based on treatment window |

Markers **love this section** because it shows critical thinking.

---

## 3.3 Simulation Implementation

Describe the **SimPy architecture**.

Typical components:

* Environment
* Patient process
* Activities as delays
* Scenario parameters

Example explanation:

> The model was implemented using the SimPy discrete event simulation framework. Each patient was represented as a process moving sequentially through pathway activities. Activity durations were sampled from statistical distributions based on values reported in the original paper.

You can include a **small code snippet**, but keep most code in the appendix.

---

## 3.4 Model Parameters

Present the key inputs.

Example table:

| Parameter         | Value          | Source             |
| ----------------- | -------------- | ------------------ |
| EMS response time | Lognormal(μ,σ) | Lahr et al.        |
| CT scan delay     | Mean 20 min    | Lahr et al.        |
| Treatment window  | 4.5 hours      | Clinical guideline |

---

## 3.5 Experimental Design

Explain **how the simulation was run**.

Example:

* Number of patients simulated
* Random seeds
* Number of replications
* Performance metrics

Example metrics:

* Door-to-treatment time
* % receiving thrombolysis
* Time to treatment

---

# 4. Results

Start simple.

---

## 4.1 Baseline Model Outputs

Show:

* mean treatment time
* % treated

Use tables and charts.

Example:

| Metric         | Simulation | Paper  |
| -------------- | ---------- | ------ |
| % thrombolysis | 12.8%      | 13.1%  |
| Mean OTT       | 92 min     | 95 min |

---

## 4.2 Comparison with Published Results

Explain:

* Where results match
* Where they differ

Possible reasons:

* Parameter ambiguity
* distribution assumptions
* implementation differences

---

# 5. Discussion

This is where **top marks happen**.

Discuss:

### Model reproducibility

Was the paper reproducible?

### Documentation gaps

What information was missing?

Examples:

* distribution parameters
* exact routing logic
* treatment eligibility criteria

### Simulation limitations

Example:

* no resource constraints
* simplified arrivals
* limited validation

### Strengths of the recreation

Example:

* transparent code
* modular SimPy structure
* reproducible notebook

---

# 6. Conclusion

Very short.

Example:

> This study demonstrated that the stroke thrombolysis model described by Lahr et al. (2013) can be recreated using Python and SimPy. While the recreated model produced broadly similar results, several assumptions were required due to incomplete reporting in the original study. The findings highlight both the potential and limitations of reproducing healthcare simulation models from published descriptions.

---

# 7. References

Standard academic references.

---

# 8. Technical Appendix

This is where the **Jupyter notebook goes**.

Include:

* full code
* parameter definitions
* test outputs

Markers expect **clean and readable notebooks**.

---

# Why this structure scores well

It demonstrates:

✔ understanding of DES
✔ critical thinking about modelling assumptions
✔ reproducible science
✔ good scientific communication

This is exactly what the assignment brief emphasises.

---

# One More Tip (Very Important)

Add a **short subsection in Methods called:**

## Iterative Model Development

Explain that you built the model in stages:

1. arrival process
2. pathway structure
3. activity times
4. treatment logic
5. validation

This aligns directly with the assignment brief.
