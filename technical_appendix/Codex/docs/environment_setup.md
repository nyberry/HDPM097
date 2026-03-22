# Environment Setup

The submission branch now uses a single root-level environment for the whole repository.

## Recommended setup

From the repository root run:

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name hdpm097
```

Then open the `Codex` folder in VS Code if you want to inspect the development trail, but keep the interpreter and notebook kernel pointed at the root `.venv`.

## VS Code configuration

If Pylance shows missing imports:

1. Open the `Codex` folder itself in VS Code.
2. Run `Python: Select Interpreter` and choose the root `.venv/bin/python`.
3. Run `Developer: Reload Window`.
4. Re-open the notebook and switch its kernel to the same interpreter.

## Note

Older local environment files in this folder were part of the iterative development process and have been removed. The authoritative submission setup is the root `requirements.txt` together with the root `.python-version`.
