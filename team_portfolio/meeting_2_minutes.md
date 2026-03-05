# HPDM097 – Group Project

# Meeting 2 Minutes  

**Module:** HDPM097 – Discrete Event Simulation Project  
**Project:** Stroke Pathway Simulation using SimPy  

**Date:** 5 March 2026  
**Location:** Online  

---

## Attendees
- NB  
- LN  

## Apologies
- NA

---

## 1. Review of Progress

The team reviewed the work completed since Meeting 1.

- The **model flow logic diagram** has been developed and agreed.
- An **initial patient arrival generator** has been implemented in Python using **SimPy**.
- The code has been generated and refined using **large language models (LLMs)** as part of the group’s planned iterative development approach.

Two LLMs were tested:

- **ChatGPT 5.2**
- **Google Gemini**

Both models produced **workable Python code** for the arrivals generator. The group confirmed that the current implementation successfully simulates **patient arrivals for the model**.

---

## 2. Next Development Phase

The next stage of development will focus on modelling **patient treatment processes and resource utilisation** within the pathway.

This will include modelling:

- Treatment processes
- **Acute ward resources**
- **Rehabilitation ward resources**

Each group member will independently attempt to develop these components using **iterative development supported by LLMs**, allowing comparison of different approaches and implementations.

---

## 3. Modelling Considerations

The group identified a potential modelling challenge relating to **resource saturation**, particularly:

- What happens when **all beds are occupied**?
- How the model should handle **patients waiting for downstream capacity (bed blockers)**.

Possible approaches include:

- Introducing **queues for ward beds**
- Modelling **delayed transfers of care**
- Implementing **blocking mechanisms**

The group agreed that this issue requires further thought and experimentation before finalising the model logic.

---

## 4. LLM Selection for Final Model

During development the team is experimenting with multiple LLMs.

A decision will need to be made regarding **which LLM will be used to generate the final version of the model notebooks and technical appendix**.

This will be decided after further testing and comparison of outputs.

---

## 5. Report and Technical Appendix Structure

The group reviewed and agreed the **proposed structure of the report and supporting materials**.

Planned outputs include:

- A main academic report
- A technical appendix folder consisting of Jupyter notebooks documenting the iterative development process, and a final full working notebook

---

## 6. Next Meeting

**Proposed date:** Friday 13 March 2026  
**Proposed time:** 09:00  
**Location:** Microsoft Teams  

The time may be adjusted if required to accommodate availability.

