# Assumptions And Simplifications

This document records modelling assumptions, simplifications, and unresolved ambiguities. It should be updated whenever the implementation departs from the literal wording of the paper.

## Current assumptions

### A1. Primary recreation target

We will first attempt a faithful recreation of the paper's occupancy-based delay calculation, rather than starting with a direct bed-blocking simulation.

Reason:

- this aligns more closely with the published method and outputs

### A2. ESD capacity

ESD will initially be represented as a routing destination without explicit capacity constraints.

Reason:

- the paper states that no data were available for ESD length of stay
- the published results focus on acute and rehabilitation bed requirements

### A3. Acute mortality handling

The acute LOS table includes a "Stroke - Mortality" subgroup. Initial implementation may model this as part of the stroke pathway terminating in `other`.

Reason:

- mortality is clearly represented in acute LOS summaries
- the exact routing implementation detail is not yet fully explicit in the extracted text

### A4. Correlation between acute and rehab LOS

Acute and rehabilitation LOS will be sampled independently for a patient.

Reason:

- the paper explicitly states that no significant correlation was assumed

### A5. Development-scale runs

During development, shorter runs and fewer replications will be used than the final paper settings.

Reason:

- this keeps iteration speed practical while preserving the final validation target

### A6. Arrival-rate source

Base-case arrival rates are taken directly from Figure 2 in the paper, not reconstructed from the reported study counts.

Reason:

- the figure provides explicit mean inter-arrival times for the model streams
- these values differ slightly from rates that would be inferred from the study-period subgroup counts

## Open questions

### Q1. Exact arrival parameters

The paper text references average time between required admissions in the model diagram. These values need to be extracted and encoded explicitly.

### Q2. Detailed scenario definitions

The paper references scenario descriptions for pooling and partial pooling. Some exact parameter values may need extraction from the full text or figures.

### Q3. Ring-fencing logic

The appendix provides results for ring-fenced stroke beds, but the exact mechanism needs to be specified before implementation.

### Q4. Daily audit details

The paper states that the model produces a daily occupancy audit. We need to choose and document the precise time-of-day sampling convention used in the recreation.

### Q5. Rehab routing for `other`

The published rehab routing row for `other` is 13% to ESD and 88% to other, which sums to 101%.

Possible explanations:

- rounding in the table
- transcription error in the appendix

Current handling:

- preserve the published values in the parameter registry
- document the discrepancy
- decide at implementation time whether to normalise for sampling
