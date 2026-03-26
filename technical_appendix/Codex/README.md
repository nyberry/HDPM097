# Stroke Pathway DES Recreation

This repository contains a staged recreation of the stroke pathway discrete-event simulation described in:

- Monks et al. (2016), "A modelling tool for capacity planning in acute and community stroke services"

The work is organised to satisfy both goals of the assignment:

1. Build an understandable Python 3.11 + SimPy 4.1.1 model.
2. Preserve a clear research record of prompts, iterations, tests, assumptions, and results.

## Final Structure

- `stroke_sim/`
  The Python package containing the recreated model and analysis logic.
  Key modules include:
  - `model.py`: parameter-driven occupancy audit simulation
  - `runner.py`: replication helpers and scenario execution
  - `metrics.py`: occupancy and delay calculations plus plotting
  - `validation.py`: published comparison targets and table helpers
  - `pooling.py`: pooled-bed scenario calculations
  - `parameters.py`: encoded paper parameters

- `notebooks/`
  The full notebook trail from early setup through scenario analysis.
  The most important notebook for submission is:
  - `10_final_technical_appendix.ipynb`
    This is the consolidated end-to-end technical appendix notebook.
  Earlier notebooks `01_...` to `09_...` remain as the development and validation trail.

- `docs/`
  Project documentation and source extracts.
  Important files:
  - `source_text/`: authoritative text versions of the brief, paper, and appendix
  - `paper_to_model_spec.md`: structured extraction of model logic from the source materials
  - `assumptions.md`: documented assumptions, simplifications, and unresolved ambiguities
  - `report_validation_section.md`: reusable report wording for validation results
  - `figures/`: generated output figures from the recreated model

- `tests/`
  Automated tests for the core model, parameters, metrics, scenarios, pooling logic, and validation table helpers.

- `.vscode/settings.json`, `pyrightconfig.json`
  Workspace configuration to help the package resolve correctly in the IDE.

## Final Notebook

Run [10_final_technical_appendix.ipynb](notebooks/10_final_technical_appendix.ipynb) for the consolidated technical appendix narrative. It includes:

- environment setup guidance
- reproducibility notes and fixed random seed
- the base occupancy distribution figure
- the acute delay trade-off curve
- current admissions validation
- `5% more admissions`
- pooled-bed scenarios
- `no complex neurological patients`
- ring-fenced acute stroke beds

The notebook is designed to run end to end from the project environment and writes final figure files into `docs/figures/`.

## Generated Outputs

Important generated figures include:

- [final_appendix_acute_occupancy_distribution.png](docs/figures/final_appendix_acute_occupancy_distribution.png)
- [final_appendix_acute_delay_tradeoff.png](docs/figures/final_appendix_acute_delay_tradeoff.png)

Additional scenario-specific figures and tables are preserved in the iteration notebooks.

## Environment

- Python 3.11 for the submission environment
- SimPy 4.1.1

Use the root-level `requirements.txt` for dependencies and the root `README.md` for setup instructions.
