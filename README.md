# HDPM097 Assignment Repository

This repository contains the submission materials and supporting development trail for the DES recreation study based on Monks et al. (2016), *A modelling tool for capacity planning in acute and community stroke services*.

## Submission-facing structure

The main submission artefacts are organised at the repository root:

- `report.md`
  Draft report text for the written submission.
- `technical_appendix/`
  Jupyter notebooks, Python code, figures, and environment files for the technical appendix.
- `team_portfolio/`
  Evidence of group working.
- `assets/figures/`
  Supporting figures used in the report.

## Main appendix to assess

The cleanest appendix entry point for a marker is:

- `technical_appendix/final_appendix/notebooks/10_final_technical_appendix.ipynb`

The `technical_appendix/final_appendix/` folder contains:

- `notebooks/`
  The consolidated end-to-end appendix notebook.
- `stroke_sim/`
  The recreated simulation package.
- `tests/`
  Automated checks for the recreated model.
- `docs/`
  Source texts, assumptions, model specification, and generated figures.
- `environment/`
  Reproducibility files targeting Python 3.11 and SimPy 4.1.1.

## Supporting development trail

The earlier tool-specific development trails are preserved in:

- `technical_appendix/Gemini/`
- `technical_appendix/Claude/`
- `technical_appendix/Codex/`

These folders support the research narrative comparing manual and AI-assisted iterative recreation workflows.

## How a marker should run the appendix

1. Start in `technical_appendix/final_appendix/`.
2. Follow `environment/README.md`.
3. Create a Python 3.11 virtual environment.
4. Install `environment/requirements.txt`.
5. Run `notebooks/10_final_technical_appendix.ipynb` from top to bottom.

## Note

This branch still preserves intermediate development material because the assignment brief asks for evidence of iterative model recreation. For assessment, `technical_appendix/final_appendix/` is the intended primary appendix package.
