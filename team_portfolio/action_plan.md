# HPDM097 – Coursework 2  
## Action Plan and Milestones  
Project Duration: 4 Weeks  
Group Size: 3  

---

# 1. Project Aim

To recreate (or simplify and recreate) a published healthcare discrete-event simulation model using Python and SimPy, following an iterative research methodology. The project will investigate the feasibility of model recreation from published text and (optionally) the effectiveness of LLM-assisted prompt engineering.

---

# 2. High-Level Timeline (4 Weeks)

| Week | Focus | Outputs |
|------|-------|---------|
| Week 1 | Paper selection + model understanding | Selected paper, model activity diagram, task allocation |
| Week 2 | Model design + initial implementation | Iteration 1 & 2 notebooks (arrivals + core process) |
| Week 3 | Full model build + validation | Working model, test suite, replication framework |
| Week 4 | Experiments + report writing + refinement | Final model, results tables, full report draft |

---

# 3. Meeting Schedule

## Meeting 1 (End of Week 1)
**Objectives:**
- Select final paper
- Produce activity/resource/routing diagram
- Identify available data in paper
- Identify gaps and required assumptions
- Define simplifications
- Allocate individual responsibilities

**Deliverables after Meeting 1:**
- Confirmed paper selection
- Draft process diagram (in /assets)
- Initial parameter extraction table
- Individual work plan for Week 2

---

## Meeting 2 (End of Week 2)
**Objectives:**
- Review Iteration 1 (arrivals)
- Review Iteration 2 (core process/resource logic)
- Review prompt engineering logs
- Identify implementation issues
- Refine testing strategy
- Plan validation experiments

**Deliverables after Meeting 2:**
- Working partial model
- Defined test suite
- Clear replication strategy
- Updated simplification log

---

## Meeting 3 (End of Week 3)
**Objectives:**
- Review full model implementation
- Review validation against published results
- Review replication runs
- Identify discrepancies
- Plan final experiments
- Assign report sections

**Deliverables after Meeting 3:**
- Finalised model logic
- Experimental results ready
- Draft figures
- Structured report outline

---

# 4. Week-by-Week Detailed Plan

---

## Week 1 – Model Understanding & Planning

### Task 1: Extract Model Logic
- List all patient types
- List all activities
- List all resources
- Define routing logic
- Create process flow diagram

### Task 2: Extract Data
- Arrival distributions
- Service time distributions
- Routing probabilities
- Capacity parameters
- Performance metrics

### Task 3: Identify Gaps
- Missing parameters?
- Undefined distributions?
- Ambiguous routing rules?

### Task 4: Define Simplifications
- Remove complex scheduling?
- Reduce patient types?
- Use simpler distributions?
- Exclude rarely-used pathway components?

### Task 5: Draft SimPy Architecture

Proposed structure:

- `class Patient`
- `class StrokeModel` (or WardModel)
- `generate_arrivals()`
- `patient_process()`
- `run_replication()`
- `run_experiment()`

Define:
- How replications will be run
- How results will be stored
- How tests will be implemented

---

## Week 2 – Iterative Build (Core Simulation)

### Iteration 1
- Implement arrival process only
- Validate inter-arrival times
- Unit tests for distribution correctness

### Iteration 2
- Add main activity (treatment or bed occupancy)
- Add resources if applicable
- Test queue behaviour
- Regression test arrivals

### Prompt Engineering Research
- Log all prompts
- Record failures
- Record corrections
- Compare LLM vs manual coding

Deliverable:
- Working partial model
- Documented test results

---

## Week 3 – Full Model + Validation

### Iteration 3
- Add remaining activities
- Add routing logic
- Add conditional treatment logic
- Add performance metric calculation

### Validation
- Compare outputs to published results
- Check:
  - Mean outcomes
  - Proportions
  - Delay rates
  - Treatment rates

### Replication Framework
- Implement multiple replications
- Implement warm-up period (if needed)
- Calculate mean + confidence intervals

Deliverable:
- Fully functional model
- Validation comparison table

---

## Week 4 – Experiments + Write-Up

### Experiments
- Reproduce at least 2 scenarios from paper
- Sensitivity analysis (if time allows)

### Report Writing
Divide into sections:

Member A:
- Introduction + model design

Member B:
- Methods + prompt engineering process

Member C:
- Results + validation + experiments

Collaborative:
- Discussion
- Conclusions
- Final proofreading

### Final Checks
- All notebooks run cleanly
- Environment file included
- Prompts logged with hyperlinks
- Team portfolio complete
- Word count checked

---

# 5. Role Allocation (Initial Proposal)

Member A – Model Architect
- Extract model logic
- Design SimPy structure
- Lead technical implementation

Member B – Prompt Engineering Lead
- Design and test LLM prompts
- Maintain prompt_log.md
- Compare manual vs LLM output

Member C – Validation & Testing Lead
- Design test suite
- Implement replication framework
- Validate results vs published study

(All members contribute to coding and writing.)

---

# 6. Risk Management

| Risk | Mitigation |
|------|------------|
| Paper too complex | Simplify early in Week 1 |
| LLM produces flawed code | Use incremental prompting |
| Parameter gaps | Document assumptions clearly |
| Time pressure | Freeze feature set at end of Week 3 |
| Notebook errors | Test clean environment before submission |

---

# 7. Success Criteria

The project will be considered successful if:

- The model runs without error
- It reproduces (approximately) published outputs
- Iterative development is clearly documented
- Prompt engineering research is transparent
- All notebooks are reproducible
- All assignment requirements are met