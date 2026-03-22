# Environment Setup

The submission version of this project uses a single root-level environment for the whole repository.

## Target runtime

- Python 3.11
- SimPy 4.1.1

## Recommended setup

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

## Verification

Optional automated checks can be run from the repository root with:

```bash
python -m pytest technical_appendix/final_appendix/tests
```

## Note

Older environment files inside development-trail folders reflect the iterative build process and are not required for assessment. The authoritative setup for the submission branch is the root `requirements.txt` together with `.python-version`.
