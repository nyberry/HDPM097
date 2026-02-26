## Development notes for team working on HDPM097.

## Reproducible Environment

This project uses a dedicated Conda environment to ensure reproducibility of the simulation model and experiments.

The environment is named:

    hpdm097_a2

Where:
- `hpdm097` refers to the module code
- `a2` refers to Assignment 2

To create the environment:

```bash
conda env create -f environment.yml
conda activate hpdm097_a2
jupyter lab
```

### Proposed structure:

```
root/
│
├── README.md
├── report.md
├── environment.yml  (or requirements.txt)
│
├── technical_appendix/
│   ├── 01_iteration_arrivals.ipynb
│   ├── 02_iteration_process.ipynb
│   ├── 03_iteration_full_model.ipynb
│   └── final_model.ipynb
│
├── LLM_prompts/
│   ├── 01_arrivals_prompt.md
│   ├── 02_process_prompt.md
│   ├── prompt_log.md
│
├── team_portfolio/
│   ├── action_plan.md
│   ├── meeting_agenda_1.md
│   ├── meeting_minutes_1.md
│   ├── etc...
│
└── assets/
    ├── diagrams/
    ├── figures/
    └── extracted_parameters.csv
```