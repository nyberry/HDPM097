# HDPM097 Assignment Folder

This folder contains the submission materials and supporting development trail for the recreation of the Monks et al. (2016) stroke-pathway discrete-event simulation.

These are:

- `report.md`
  Our group's report for the written submission.
- `technical_appendix/`
  Jupyter notebooks, Python code, and supporting documentation for the technical appendix.
- `team_portfolio/`
  Evidence of group working.
- `requirements.txt`
  Project environment specification.

## Main Notebook To Assess

The intended final technical notebook is:

- `technical_appendix/final_appendix/notebooks/10_final_technical_appendix.ipynb`

The `technical_appendix/final_appendix/` folder contains:

- `notebooks/`
  The appendix notebook.
- `stroke_sim/`
  The recreated simulation package.
- `tests/`
  Automated checks for the recreated model.
- `docs/`
  Source texts, assumptions, model specification, and generated figures.

### Recommended setup

From the repository root, create and activate a Python 3.11 virtual environment, then install the project dependencies:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

These steps are sufficient to run the code and tests.

If you want to run the appendix notebook in Jupyter or VS Code, also register the environment as a notebook kernel:

```bash
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
- `technical_appendix/Codex/`

These folders compare LLM-assisted and code-agent-assisted iterative workflows. All LLM prompts are included within the notebooks. This branch preserves intermediate development material because the assignment brief asks for evidence of iterative model recreation.
