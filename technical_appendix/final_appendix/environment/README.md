# Environment

This technical appendix is intended to be run with:

- Python 3.11
- SimPy 4.1.1

## Setup

From `technical_appendix/final_appendix/` run:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
python -m ipykernel install --user --name hdpm097-stroke
```

Then select the `hdpm097-stroke` kernel in Jupyter or VS Code.

## Run order

1. Activate the virtual environment.
2. Open `notebooks/10_final_technical_appendix.ipynb`.
3. Run the notebook from top to bottom.

## Notes

- `notebooks/10_final_technical_appendix.ipynb` is the consolidated appendix notebook intended for assessment.
- The environment files here are submission-oriented and are designed to help a tester recreate the runs with minimal manual intervention.
