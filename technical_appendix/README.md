# Technical Appendix Overview

This folder contains both the development trail and the final appendix-ready materials for the DES recreation study.

## Main final appendix

Use:

- `final_appendix/notebooks/10_final_technical_appendix.ipynb`

This is the consolidated notebook that runs the recreated model end to end and presents:

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

## Supporting development trails

The project also preserves tool-specific development history:

- `Gemini/`
- `Claude/`
- `Codex/`

These folders are useful for showing how the recreation process differed across LLMs and coding workflows.
