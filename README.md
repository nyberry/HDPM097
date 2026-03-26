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

## Final Technical Appendices

The intended final technical appendices are:

- `technical_appendix/final_appendix/notebooks/final_appendix_gemini.ipynb`
- `technical_appendix/final_appendix/notebooks/final_appendix_codex.ipynb`

This submission provides two final appendix notebooks rather than a single consolidated notebook. This is deliberate and reflects the comparative design of the assignment. The project did not simply aim to recreate the Monks et al. model once; it aimed to compare how that recreation proceeded under two different AI-assisted workflows. Keeping separate final appendices preserves that distinction more clearly for a marker, because each notebook shows the full end-to-end logic, outputs and validation results for one workflow without collapsing the methodological differences between them. In other words, two final appendices better support the research question of the assignment than one merged appendix would.

The `technical_appendix/final_appendix/` folder contains:

- `notebooks/`
  The two final appendix notebooks, one for Gemini and one for Codex.
- `stroke_sim/`
  The recreated simulation package.
- `tests/`
  Automated checks for the recreated model.
- `docs/`
  Source texts, assumptions, model specification, and generated figures.

### Recommended setup

This project was developed for Python 3.11 and SimPy 4.1.1. It is expected to run on Python 3.11 or newer, provided the dependencies in `requirements.txt` install successfully.

From the repository root, create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
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

- `technical_appendix/final_appendix/notebooks/final_appendix_gemini.ipynb`
  or
- `technical_appendix/final_appendix/notebooks/final_appendix_codex.ipynb`

and select the `hdpm097` kernel.

## Suggested run order for a marker

1. Create and activate the root virtual environment.
2. Install `requirements.txt`.
3. Open `technical_appendix/final_appendix/notebooks/final_appendix_gemini.ipynb`.
4. Run the notebook from top to bottom.
5. Open `technical_appendix/final_appendix/notebooks/final_appendix_codex.ipynb`.
6. Run the notebook from top to bottom.
7. If desired, run the automated checks with `python -m pytest technical_appendix/final_appendix/tests`.

## Supporting development trail

The earlier tool-specific development trails are preserved in:

- `technical_appendix/Gemini/`
- `technical_appendix/Codex/`

These folders compare LLM-assisted and code-agent-assisted iterative workflows. All LLM prompts are included within the notebooks. This branch preserves intermediate development material because the assignment brief asks for evidence of iterative model recreation.
