# HDPM097 Discrete Event Simulation Project

## Meeting 3 Minutes

**Date:** Friday 13 March 2026
**Time:** 3.30pm 
**Location:** Online

### Attendees

* Nick A.
* Nick B
* Luqman

---

## 1. Progress Update

Since Meeting 2, the group has continued iterative development of the simulation model using several large language models (LLMs), including **ChatGPT, Gemini, and Claude**.

Using this approach, the team has successfully generated code to model:

* **Patient arrival processes**
* **Patient flow through the system**
* **Resource utilisation for the acute ward**
* **Resource utilisation for the rehabilitation ward**

The model currently produces an outcome measure corresponding to the **probability of delay**, consistent with the key metric described in the **Monks et al.** paper.

---

## 2. Issues Identified

Although the model is now functionally simulating patient arrivals and ward resources, the group noted several concerns:

* The **codebase has become increasingly complex** due to multiple iterations of LLM-generated code.
* The **simulation outputs do not match the published results from the paper precisely**.
* At present, it is **unclear which aspects of the model logic or parameterisation are responsible for these discrepancies**.

The group discussed that the current level of code complexity may be making the model difficult to validate and debug.

---

## 3. Agreed Approach

The group agreed that it would be beneficial to **step back and simplify the modelling approach**.

Specifically, the team agreed to:

* Attempt to generate **simpler simulation code** using LLMs.
* Provide the LLMs with **examples of the style and level of complexity used in the course workshops** to guide code generation.
* Focus on building **clean, understandable simulation models**, even if they represent **simplified versions of the original paper model**.

The objective is to produce models that:

* Are **transparent and easy to interpret**
* Remain **faithful to the key structure of the Monks et al. model**
* Successfully reproduce the **core outcome measure (probability of delay)**.

---

## 4. Goals Before Next Meeting

The group aims to:

* Develop **working simulation models with reduced complexity**
* Ensure the models can still generate the **key delay probability outcomes**
* Continue **iterative model development using LLM assistance**
* Update the **project report and documentation** to reflect current progress.

---

## 5. Actions

| Action                                                                                                   | Owner |
| -------------------------------------------------------------------------------------------------------- | ----- |
| Continue iterative model development using LLMs with simplified prompts and workshop-style code examples | All   |
| Continue updating the project report and technical appendix                                              | All   |

---

## 6. Next Meeting

**Date:** Friday 20 March 2026
**Time:** 3:30 pm
**Location:** Online
