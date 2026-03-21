# Assignment Brief
Assignment Brief - Coursework 2
Module Title: Making a
Difference
with Health
Data
Module Convenor: Thomas Monks
Module Code: HPDM097 Summative/Formative Summative
Module Credits: 30 Assignment Type: Group
% of Module Mark: 50% Date Set: 13/01/2026
Date Due: 27/03/2026
1 Required Task
The vast majority of Discrete-Event Simulation (DES) models used to analyse health problems are
published in academic journal articles as text descriptions only. That is, the computer model -
the code - is not available to anyone but the original study authors; however, a description of the
model logic and data are provided in writing. The recreation of computer models from these natural
language descriptions is non-trivial and requires a specialist with DES training.
• In this assignment, you will work in a group (size 2 or 3) to select an academic journal article
reporting a DES model applied to a health problem. You will then conduct a research study
to test if it is possible to recreate the simulation model (or a simplified version of it) in python
and ‘simpy’.
• You are permitted to manually write the simulation code yourselves in python, and/or conduct experiments with Large Language Models (LLM; e.g. ChatGPT, Claude, or Gemini) to
investigate their ability to recreate models in python.
• You are required to produce a report documenting your research study, results, and conclusions.
You must also provide a technical appendix (one or more Jupyter notebooks) containing the
Python code and all prompts given to a LLM.
1
2 Assignment components
Please submit a single .zip file to ELE containing the following:
1. A report of your research study to recreate a DES model (see Section 4.1 for requirements)
2. A technical appendix: a well formatted and annotated Jupyter notebook(s) of the full
simulation model and any prompts to an AI tool. (see Section 4.2 for requirements).
3. Evidence of group working:
• As this is a group assignment, we want to see evidence that the group operated in a
manner similar to what would be expected in a professional environment. Therefore, we
are requiring that you submit a portfolio of documents to showcase this.
– Meeting agendas (x3)
– Meeting minutes; including attendees and actions assigned to individuals (x3)
– Action plan with milestones
3 Advice on the recreation of DES models
Figure 1 illustrates a general recommended approach for how a model can be recreated manually
or by using an LLM. In both cases, it is recommended to take an iterative approach to model
development. In each iteration, additional detail is added to the simulation model. This is followed
by a series of tests that are conducted to check if the new model logic is implemented as expected
and also to test that the new logic does not break anything already implemented. Document and
record everything you do with care.
3.1 General advice on getting started
It is recommended that groups follow this process to get started:
1. Carefully read a paper and produce a list or diagram of all of the activities (e.g., treatment),
resources, and routing that patients follow in the model.
2. List what data are reported in the paper (such as parameters for statistical distributions) and
if any assumptions or simplifications are needed.
3. Before writing or generating any code, discuss and plan simplifications in the model logic, and
a potential design for the model code in ‘simpy’ (e.g. classes, functions, Experiment classes,
how to run multiple replications)
3.2 How to add detail to the model
Building the model in one go will be difficult. It is recommended that the groups add detail step by
step. For example:
• Step 1: Write code for generating one or more types of patient arrivals to the health care
system.
• Step 2: Test the arrival processes. If all tests pass, proceed to step 3.
2
Figure 1: A recommended iterative approach to recreating models manually or with the aid of an
LLM.
• Step 3: Write code where patients undergo treatment or queue and take resources.
• Step 4: Test that the treatment process works as expected. Retest the arrival process.
3.3 How to use a Large Language Model in your research
LLMs are hard to use for specialist data science applications. If you choose to use one then your
research should focus on ‘prompt engineering’. A prompt is the query string that you provide to
the chat interface of the LLM. Current LLM’s cannot cope with all of the text from an academic
paper and the natural language in the paper may be too ambiguous for an LLM to generate code
that you might expect. Groups are advised to do the following:
• Limit the size of prompts, by designing ones that generate and modify code incrementally.
For example, if your model has multiple activities, add these in one at a time using multiple
prompt and testing cycles.
• Be specific about python libraries that you wish to use.
• Be consistent with terminology used within a single prompt or in subsequent prompts. For
example, if you have initially used the term ‘treatment time’ to define a patient activity in
a ward then you should always refer to ‘treatment time’ and avoid alternative terms such as
‘length of stay’.
• Take extra care to provide prompts that define logic clearly. For example define steps taken
in a function in a numbered list or use clear terminology for if/else logic.
3
Groups are reminded that LLM’s can make mistakes and may be trained on code that may
contain obvious or subtle bugs. Test your code incrementally. If you find bugs you could attempt
to identify the problem in your original prompt and re-engineer it; prompt the LLM to fix the bug;
or fix the bug manually. This is a research project so keep a detailed log of what you have
done and think critically about what types of prompts work and what types don’t work
for recreating DES models.
See sections 4.1 and 4.2 for advice on what to document and how to report it.
3.4 Where to find academic journal articles
Groups are free to choose their own article. To help, several example journal articles are provided
and groups are allowed to use these for their project.
• Penn, M. L., Monks, T., Kazmierska, A. A., & Alkoheji, M. R. A. R. (2019). Towards generic
modelling of hospital wards: Reuse and redevelopment of simple models. Journal of Simulation,
14(2), 107–118. https://doi.org/10.1080/17477778.2019.1664264
• Lahr, Maarten M.H. et al. (2013) A Simulation-based Approach for Improving Utilization of Thrombolysis in Acute Brain Infarction. Medical Care 51(12):p 1101-1105, DOI:
10.1097/MLR.0b013e3182a3e505 https://doi.org/10.1097/MLR.0b013e3182a3e505
• J D Griffiths, M Jones, M S Read & J E Williams (2010) A simulation model of bed-occupancy
in a critical care unit, Journal of Simulation, 4:1, 52-59, DOI: https://doi.org/10.1057/jos.
2009.22
• Monks, T. et al. , ”A modelling tool for capacity planning in acute and community stroke services,” BMC Health Serv Res 16, 530 (2016). https://doi.org/10.1186/s12913-016-1789-4
Penn et al. includes two DES models of hosptial wards (one general one Intensive Care).
The models were created in a DES package called Simul8. The Simul8 model for the general ward
and example parameters are included in an online appendix (in an Excel file). The queuing in the
general ward model has to deal with the added complexity that NHS wards separate male and female
patients.
Lahr et al. used a commercial DES package called PlantSim to investigate acute stroke provision
in the Netherlands. It has a non-typical approach to simulation where a fixed number of patient
journeys are simulated as opposed to using multiple replications. No queuing is included. You can
find detailed data in the online appendix. No computer model is available to the public.
Griffiths et al. is a relatively simple and classical model of a Critical Care Unit in the UK. It
was coded in VBA and has never been made available. It has a detailed description of the model
and most of its parameters; although some assumptions will have to be made about distributions.
For example, where empirical data was used instead of a statistical distribution.
Monks et al, used a commercial DES package called Simul8 to build a simple generic model
of acute stroke and rehabilitation capacity. It has a clear logic diagram and good documentation of
parameters. An option for simplification is to focus only on the acute stroke service. The Simul8
computer model is not available to the public.
Alternatively you may wish to search the literature for a suitable healthcare DES model. It is
recommended that you pick a model with low to medium levels of complexity. For example, models
that have relatively simple queuing processes, resource usage, and are limited in scope. To help your
search you may wish to consult one of the following sources:
4
• The Healthcare Applications track in Winter Simulation Conference archives. https:
//informs-sim.org/
• The Journal of Simulation archives https://www.tandfonline.com/journals/tjsm20
For any model selected, groups are also permitted to simplify the model reported in the academic
paper. For example,
• Remove complex booking/scheduling rules in favour of simpler queuing,
• Reduce the number of activities included in a model,
• Model a single type of patient instead of multiple types of patients (e.g. a general stroke
patient versus patients with severe, moderate and mild stroke),
• Choose to use a simple statistical distribution (e.g. Log Normal) instead of a complex phase
type distribution.
All simplifications must be documented and justified in the report. At a minimum your
model design should either have one type of patient and multiple activities; or multiple
types of patient and one activity.
4 The report and technical appendix
4.1 The report
The report is a write up of your research study attempting to recreate a DES model. It should include
an abstract (or summary), introduction, methods, results, discussion, conclusions and references.
The report should not exceed 2000 words including the abstract. Please ensure that it is written in
good quality English and is free from spelling mistakes.
4.1.1 Abstract
An abstract should be no more than 200 words. It should summarise objectives, methods, results
and conclusions.
4.1.2 Introduction
The introduction should list your research questions, cite the journal article, briefly introduce
the design of the DES model that you are recreating (for example, a description and diagrams of
model logic), and describe any assumptions, or simplifications that you are required to make due to
inadequate reporting in the academic article.
4.1.3 Methods
Methods should describe the process you used for recreating the model (e.g what LLM(s) were used,
the process for prompt engineering, types of tests used), what data you recorded/captured at each
iteration of the model (e.g. number and functions of tests), how you will measure success/failure
(e.g. what tests should the final model pass to be considered a recreation of your model design?),
and how you handled any unexpected problems you encountered. Cite any journal articles, websites,
and sources that you used to design your study and methods.
5
4.1.4 Results
Results should be brief and report the data and success/failure criteria described in your methods.
Text, tables and charts may be used. Results may include, but are not limited to:
• a description of the final model, how to use it, example output from the model, and if you
were successful or not in your aims to recreate the design in the introduction.
• report how many iterations were needed to recreate the model.
• number of tests failed at each iteration and rework
Results tables will not count towards your word count.
4.1.5 Discussion
The discussion provides an opportunity for groups to reflect on the project. Groups may consider:
• what were the problems in reporting in the paper that prevented, limited or aided their recreation of the model? What were the positive aspects of the paper that aided recreation?
• what could the authors of the article have done to improve their model documentation to aid
recreation?
• giving more context to their prompt engineering and provide examples of prompts that worked
and prompts that did not work to generate acceptable code. (Note: example prompts will not
count towards total word count).
• what were the challenges with using an LLM and how were these overcome?
• what are the limitations of their results and method?
• what would they do or record differently if they could re-design their methods and start again?
• if there is any recent literature in recreating models (of any type) that has similar or different
findings.
4.1.6 Conclusion
A brief paragraph with concluding remarks to the study.
4.1.7 References
References should use the Vancouver (numbered) reference style. References do not count towards
the 2000 word limit.
6
4.2 Technical Appendix
The appendix should include a well formatted and annotated Jupyter notebook of the full simulation
model. The notebook should demonstrate either how the model is used, or its current deficiencies if
it is not possible to fully recreate the model.
If an LLM has been used in an iterative manner to support recreation of the model then each
iteration should have its own notebook. These notebooks should contain the aim of the prompt,
the full prompt given to the LLM, the code (and any text) generated by the LLM, testing of the
code, and tester notes. Please name the notebooks so that the order of prompts is obvious (e.g.
01_iter.ipynb, 02_iter.ipynb ...).
It must be possible to run your Jupyter notebooks. Please error check them and provide details
of a virtual environment to use.
4.3 Marking criteria
Marking is split into two components
4.3.1 Evidence of group working (10%)
Please note that the evidence of group working will not be marked for content but compliance only.
Therefore, if you submit all the documents and they are fit for purpose you will receive the full 10%
for this component.
4.3.2 Simulation research study (90%)
A detailed breakdown of these criteria is available at the end of the document.
1. The design and execution of the research study.
2. The quality of the report.
3. The quality of the technical appendix.
5 Marking Scheme
The design and execution of the research study
• 0 - 49: Absent or limited evidence of appropriate design and an unclear method for conducting the research. The simulation model design does not meet the minimum complexity
specification.
• 50 - 59: Limited but mostly appropriate study design and method for conducting the research.
• 60 - 69: Generally appropriate study design and method for recreating an appropriately
complex simulation model. A rationale for the study methods is presented, but has some areas
of ambiguity or easily overcome limitations.
• 70 - 85: An appropriate and study design and clear method for recreating an appropriately
complex simulation model. A strong rationale for the study methods is presented, all but the
most challenging aspects of appropriate research methodology are included.
7
• 86 - 100: A research standard study design that is informed by the literature and attempts
to manage potential method limitations seen elsewhere.
The quality of the report
• 0 - 49: Absent or poor quality report that writes up the study, containing a large number of
grammatical and typographical errors. The report exceeds the word limit by more than 10%.
• 50 - 59: Borderline passable report that writes up the study. The report contains multiple
grammatical and typographical errors.
• 60 - 69: Generally good report that attempts to take account of all requirements specified.
The report may contain grammatical and typographical errors.
• 70 - 85: An excellent report that takes account of all requirements specified. The report has
minimal grammatical and typographical errors.
• 86 - 100: Publication quality write-up of the research that accounts for all aspects of the
specification.
The quality of the technical appendix
• 0 - 49: Absent or unintuitive technical appendices. The code in the appendix cannot be run
by a marker.
• 50 - 59: Borderline passable technical appendices. Demonstration of limited understanding
of how to create Jupyter notebooks, organise code, and follow best practice. The code in the
appendix can be run by a marker with some manual intervention.
• 60 - 69: Generally good technical appendices. Demonstration of understanding of how to
create Jupyter notebooks, organise code, and follow most aspects of coding best practice. The
code in the appendix can be run by a marker without the need for manual intervention, but
may not follow best practices.
• 70 - 85: Excellent technical appendices that demonstrate a solid understanding of how to
create Jupyter notebooks, organise code, and follow best practice. The code in the appendix
is easy to run and follows best practice.
• 86 - 100: Publication quality Jupyter notebooks that are easily understood, and navigated
by someone who did not create them. All code dependencies are simple to manage and the
notebooks can be reused to recreate the results of the study.