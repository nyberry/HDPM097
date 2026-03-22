# HDPM097 Assignment Repository

This repository contains the submission materials and supporting development trail for the recreation of the Monks et al. (2016) stroke-pathway discrete-event simulation, together with a comparison of manual and LLM-assisted iterative design workflows.

## Submission-facing structure

The main submission artefacts are organised at the repository root:

- `report.md`
  Draft report text for the written submission.
- `technical_appendix/`
  Jupyter notebooks, Python code, figures, and supporting documentation for the technical appendix.
- `team_portfolio/`
  Evidence of group working.
- `assets/figures/`
  Supporting figures used in the report.
- `requirements.txt`
  Single project environment specification for markers and testers.
- `.python-version`
  Python version target for reproducible setup.

## Main appendix to assess

The primary appendix entry point is:

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

## One environment for the whole project

Use a single root-level Python environment for the whole repository.

### Recommended setup

From the repository root run:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name hdpm097
```

Then open:

- `technical_appendix/final_appendix/notebooks/10_final_technical_appendix.ipynb`

and select the `hdpm097` kernel.

## Suggested run order for a marker

1. Create and activate the root virtual environment.
2. Install `requirements.txt`.
3. Open `technical_appendix/final_appendix/notebooks/10_final_technical_appendix.ipynb`.
4. Run the notebook from top to bottom.
5. If desired, run the automated checks with `python -m pytest technical_appendix/final_appendix/tests`.

## Supporting development trail

The earlier tool-specific development trails are preserved in:

- `technical_appendix/Gemini/`
- `technical_appendix/Claude/`
- `technical_appendix/Codex/`

These folders support the research narrative comparing manual and AI-assisted iterative recreation workflows. Their local environment files reflect development history and are not required for assessment.

## Note

This branch preserves intermediate development material because the assignment brief asks for evidence of iterative model recreation. For assessment, the root `requirements.txt` and the appendix notebook in `technical_appendix/final_appendix/` are the intended primary entry points.
