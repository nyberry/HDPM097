I want you to help me generate python code to simulate the arrival and flow of patients through a hospital stroke pathway.

This will be an iterative process. In this first iteration, please only generate the code to simulate arrivals. Later we model the flow of patients through the hospital wards. 

Use python 3.11 and SimPy 4.1.1

Patients are classified into 4 groups: Stroke, TIA, Complex neurological and other.

Over the base period, the following number of patients were seen:
- Acute stroke, n = 1320
- TIA, n = 158
- complex neurological, n = 456
- other, n = 510
Please maintain these proportions in the simulation model.

New patients should arrive with the following mean inter-arrival times:
- Acute stroke, 1.2 days
- TIA, 9.3 days
- Complex neurological, 3.6 days
- other, 3.2 days
For all groups, the time between arrival of new admissions should be modelled using an exponential probability distribution.

Construct a function to allow the generation of new patients. The function should accept parameters for the length of the simulation in days, and which categories of patient to yield. The default should be to yield patients from all categories. Include a helper function for sampling from an exponential distribution.

---

Please make the following refinements to the code you have generated:

1. A Scenario class. It is good practice to pass all of the parameters to the simulation model in a container. A class is a flexible way to achieve this aim. Hard code the data representing the base case. mMakes use of the default parameters to set up the base case scenario. 

2. Extend the sampling helper function use distribution classes. Define the following classes: Exponential and Lognormal. It is important to be able to pass random_seed when instantiating a new distribution instance.

3. Add a utility function trace(msg), for selectively printing the output of simulation in the console. Set a TRACE constant to FALSE to turn printing off, and TRUE to turn printing on.

---
*Development conducted with ChatGPT 5.2. These prompts are documented as part of the group's evidence of working*