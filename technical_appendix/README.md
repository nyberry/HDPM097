# Technical Appendix Overview

This folder contains both the development trail and the final appendix-ready materials for the DES recreation study.

## Main Final Appendices

Use:

- `final_appendix/notebooks/final_appendix_gemini.ipynb`
- `final_appendix/notebooks/final_appendix_codex.ipynb`

These are the two submission-facing appendix notebooks. They are presented separately to preserve the comparative design of the project: one notebook documents the final Gemini-based recreation workflow and the other documents the final Codex-based recreation workflow. Keeping them separate makes it easier for a marker to compare the two AI-assisted approaches directly, rather than reading a merged appendix in which the methodological differences are less visible.

Together, the two notebooks present:

- environment and reproducibility notes
- the acute occupancy figure
- the acute delay trade-off curve
- current-admissions validation
- `5% more admissions`
- pooled-bed scenarios
- `no complex neurological patients`
- ring-fenced acute stroke beds

## Reproducibility

Use the single root-level environment described in:

- `../README.md`

From the repository root, create the Python 3.11 environment and install `requirements.txt`, then run the final appendix notebook.
From the repository root, create the environment and install `requirements.txt`, then run both final appendix notebooks.

## Supporting development trails

The project also preserves tool-specific development history:

- `Gemini/`
- `Claude/`
- `Codex/`

These folders are useful for showing how the recreation process differed across LLMs and coding workflows.
