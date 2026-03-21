# Environment Setup

This project targets Python 3.11 or newer for local development, while the assignment brief still specifies Python 3.11 as the intended runtime.

## Expected local setup

- Python 3.11 installed on the machine
- a local virtual environment at `.venv/`
- VS Code opened at the `Codex` folder as the workspace root

## Create the environment

If you want to use your current interpreter:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## VS Code configuration

The workspace is configured to expect the interpreter at:

```text
.venv/bin/python
```

Files supporting this:

- `.vscode/settings.json`
- `.python-version`
- `pyrightconfig.json`

## If Pylance still shows missing imports

1. Open the `Codex` folder itself in VS Code.
2. Run `Python: Select Interpreter` and choose `.venv/bin/python`.
3. Run `Developer: Reload Window`.
4. Re-open the notebook and switch its kernel to the same `.venv` interpreter.

## Current machine state

At the time this file was updated, the available default interpreter was Python 3.13.5. The project metadata has been relaxed to allow that interpreter for local development.
