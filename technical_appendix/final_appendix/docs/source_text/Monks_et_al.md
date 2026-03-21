# Monks et al. Appendix

A modelling tool for capacity planning in
acute and community stroke services
Thomas Monks1* , David Worthington2, Michael Allen3, Martin Pitt, Ken Stein3 and Martin A. James3
Access
Abstract
Background: Mathematical capacity planning methods that can take account of variations in patient complexity,
admission rates and delayed discharges have long been available, but their implementation in complex pathways
such as stroke care remains limited. Instead simple average based estimates are commonplace. These methods
often substantially underestimate capacity requirements.
We analyse the capacity requirements for acute and community stroke services in a pathway with over 630
admissions per year. We sought to identify current capacity bottlenecks affecting patient flow, future capacity
requirements in the presence of increased admissions, the impact of co-location and pooling of the acute and
rehabilitation units and the impact of patient subgroups on capacity requirements. We contrast these results to the
often used method of planning by average occupancy, often with arbitrary uplifts to cater for variability.
Methods: We developed a discrete-event simulation model using aggregate parameter values derived from routine
administrative data on over 2000 anonymised admission and discharge timestamps. The model mimicked the flow
of stroke, high risk TIA and complex neurological patients from admission to an acute ward through to community
rehab and early supported discharge, and predicted the probability of admission delays.
Results: An increase from 10 to 14 acute beds reduces the number of patients experiencing a delay to the acute
stroke unit from 1 in every 7 to 1 in 50. Co-location of the acute and rehabilitation units and pooling eight beds
out of a total bed stock of 26 reduce the number of delayed acute admissions to 1 in every 29 and the number of
delayed rehabilitation admissions to 1 in every 20. Planning by average occupancy would resulted in delays for one
in every five patients in the acute stroke unit.
Conclusions: Planning by average occupancy fails to provide appropriate reserve capacity to manage the variations
seen in stroke pathways to desired service levels. An appropriate uplift from the average cannot be based simply
on occupancy figures. Our method draws on long available, intuitive, but underused mathematical techniques for
capacity planning. Implementation via simulation at our study hospital provided valuable decision support for
planners to assess future bed numbers and organisation of the acute and rehabilitation services.
Keywords: Stroke, Capacity planning, Simulation, Average occupancy
Background
Management of capacity in acute and community path-
ways is complex. To analyse these systems the mathem-
atical sciences have developed a wide range of robust
analytical methods focused on queuing and patient flow,
but the uptake and implementation of these methods in
routine decision making remains limited in healthcare
compared to other sectors [1–3]. In the absence of these
models, decision makers must make capacity planning
decisions based on average occupancy of wards and, in
some cases, aware of the limitations of doing so, apply
arbitrary uplifts to these figures. Simulation modelling is
an intuitive approach to modelling that synthesises a
range of data sources to support decision making for
complex problems [4]. For capacity planning problems
simulation modelling offers a way to translate the large
knowledge base of relevant mathematical models to a
form accessible and transparent to healthcare profes-
sionals and managers.
* Correspondence: thomas.monks@soton.ac.uk
1NIHR CLAHRC Wessex, Faculty of Health Sciences, University of
Southampton, Southampton SO17 1BJ, UK
Full list of author information is available at the end of the article
© 2016 The Author(s). Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0
International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and
reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to
the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver
(http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.
Monks et al. BMC Health Services Research (2016) 16:530 The performance of acute and community stroke ser-
vices typifies the difficulties in capacity planning decisions.
Suspected stroke patients, actual stroke and mimics, re-
quire urgent access to an acute stroke unit followed by
timely transfer to early support discharge services (ESD) or
inpatient rehabilitation in a community hospital. Indeed in
the United Kingdom the performance of stroke services is
measured by the proportion of stroke patients admitted to
the stroke unit within four hours of hospital arrival and the
proportion of stroke patients that spend 90 % of their hos-
pital stay on a stroke unit, with large financial penalties for
underperforming services. Performance against these tar-
gets is influenced by three interacting factors [5, 6]– cap-
acity, variation in patient length of stay and difficulties in
discharging patients to the community (so called‘bed
blocking’). As the number of patients suffering a stroke in-
creases, the pressure on acute, ESD and community re-
habilitation services will rise, and accurate capacity
planning that delivers a cost-effective service will become
even more critical. Whilst appropriate capacity planning
techniques have been implemented and used in both car-
diothoracic surgery [5] and emergency departments (ED)
[7], they are only outlined and encouraged with respect to
stroke services [8, 9].
In any financially constrained health service there is a
need for accurate capacity planning of stroke services. The
present UK policy for the centralisation of hyperacute
stroke services [10–13] makes it especially relevant as
some stroke units will see large increases in the number of
patients admitted. Capacity planning simply using average
occupancy, even Bagust et al’s [14] suggested 85 % target
bed occupancy, is imprecise and can lead to severe delays
within the stroke pathway. Transfer delays to rehabilita-
tion negatively affect patient outcomes [15] and may have
financial penalties for hospitals. Mathematical modelling
of the whole pathway provides a rational and robust way
to mitigate against these problems.
Aims
To implement advanced capacity planning techniques
within a stroke pathway in a UK hospital, we developed a
discrete-event simulation model based on 46 months of
data (n = 2444; average 637 admissions per year) collected
between January 2010 and October 2013. The model
mimics the flow of patients from admission to an acute
stroke unit through to community rehabilitation and ESD.
We sought to identify current capacity bottlenecks affecting
patient flow; future capacity requirements in the presence
of increased admissions; the impact of co-location and
pooling of the acute and rehabilitation units; and the im-
pact of complex-neurological patients, who are also cared
for on stroke wards, on capacity requirements. We contrast
these results to the often used method of planning by aver-
age occupancy with and without small uplifts (10-40 %).
Page 2 of 8
Methods
Study setting
The stroke wards in our hospital are part of a pathway that
admits stroke (n = 1320; 54 %), high risk transient ischemic
attack (TIA; n = 158; 6 %), complex neurological (n = 456;
19 %) and other types of medical patients (n = 510; 21 %).
The acute stroke unit and single community rehab unit are
in separate geographic locations. ESD is provided to mild
to moderate severity stroke patients [16, 17] (n = 463) from
both the acute (n = 300; 63 %) or community rehabilitation
wards (n = 163; 37 %). The numbers of beds in the acute
and rehabilitation wards are currently 10 and 12
respectively.
Simulation model
Patient arrival rates, flows and occupancies of stroke units
are subject to substantial variation due to patient type and
complexity, eligibility for ESD, seasonal (daily and quar-
terly) effects, and overflow from other pressured hospital
wards. We constructed a model incorporating these varia-
tions using the simulation software SIMUL8 [18]. The
model provided a visual display of patient flows to facili-
tate explanation of its logic to clinicians. The model pa-
rameters are included in the online Additional file 1.
Our model differs from other models of stroke services
focusing on thrombolysis [19–26], as it aims to inform
decisions on capacity planning in different parts of the
system. The key premise of our model that suits its use
in capacity planning is that, unlike the real world, it al-
lows patients to flow to the appropriate ward as soon as
that is required, thereby estimating‘unfettered’ demand
[27]. The model produces a daily audit of the occupancy
of each stroke ward or service and over time constructs
the occupancy probability distribution function (PDF).
As the model has no capacity limits, daily occupancy is
Poisson distributed [28]. Figure 1 illustrates a simulated
occupancy distribution with an average of nine beds,
along with a clear indication of the variability away from
that average. Figure 2 illustrates the model’s structure
and the average admission rates of patient subgroups to
the stroke wards.
Outcome measures
The model estimates the probability that a patient can-
not be immediately admitted to the acute unit, commu-
nity rehabilitation unit or ESD. We call this estimate the
probability of delay or for shorthand p(delay). For each
scenario investigated we estimate p(delay) for a range of
bed numbers and construct a stepped trade-off curve
(see Fig. 3 for an example). The reciprocal (1/p(delay))
provides a quantity that is easily understood by clinicians
and managers. For example, p(delay) = 0.02 means that 1
in every 50 patients will experience some delay in admis-
sion or transfer.
Monks et al. BMC Health Services Research (2016) 16:530 Page 3 of 8
Fig. 1 Simulation probability density function for occupancy of an acute stroke unit
We use both the PDF and cumulative probability
density function of occupancy to calculate the prob-
ability of delay. The general form of this calculation,
often referred to as the Erlang loss formula [28], is
P(N= n)/P(N ≤ n). The calculation of the probability
of delay in a system where beds are partially pooled
between different types of patient is detailed in the
Additional file 1.
Data sources
The model was constructed using anonymised adminis-
trative data collected routinely by the healthcare pro-
vider in the acute and community settings. All patients
had a recorded primary diagnosis using ICD-10 coding.
These codes were grouped into a simpler coding
scheme of stroke (ischemic or haemorrhagic), TIA,
complex neurological and other. The‘other’ category
Fig. 2 Model diagram. Notes: the arrows illustrate the destinations that patients can flow in the model. Figures are average time between
required admissions. E.g. a stroke patient requires a bed in the acute stroke unit every 1.2 days
Monks et al. BMC Health Services Research (2016) 16:530 Page 4 of 8
Fig. 3 Simulated trade-off between the probability that a patient is delayed and the no. of acute beds available
represents medical patients who are displaced into the
stroke units due to capacity constraints elsewhere in
the hospital.
Statistical analysis
Variations in arrival of new admissions and length of
stay are modelled using probability distributions. Expo-
nential distributions are used to model the time be-
tween arrivals of new admissions while lognormal
distributions are used to model length of stay. Each of
the four patient types included in the model had their
own admission and length of stay distributions, which
also depended on the ward and on and the patient’s eli-
gibility for ESD. We assumed no significant correlation
between the length of a patient’s acute stay and re-
habilitation stay. No data were available for length of
stay in ESD. The model therefore estimates capacity re-
quirements for acute and rehabilitation beds only.
To estimate arrival and length of stay distributions we
followed standard practice in discrete-event simulation
studies (see [29, 30]). Inter-arrival times were modelled
using the exponential distribution, implying random ar-
rivals. For length of stay we used the software Stat::Fit
[31] to provide a list of candidate distributions and max-
imum likelihood estimates of parameters. We selected
the log-normal distribution from this list as it is often
used to model process times [29].
A workshop was held to review the model logic. Face
validation was sought from those that worked in the
stroke pathway; in this case a senior ED medic, a senior
stroke physician, a senior stroke nurse, the stroke path-
way manager and the hospital’ s data analyst for stroke.
Explanation of the model logic was aided by an anima-
tion of the model illustrating the flow of patients. The
workshop also provided a forum to review data used in
the model. Initial runs of the model with parameter
Scenario comparison
Table 1 lists the five scenarios used for capacity planning.
To obtain stable results each scenario has a run length of
five years and was replicated 150 times. As our model
starts with no patients occupying beds, we also include an
additional 3 year warm-up period to allow the model to
reach realistic and steady-state occupancy levels. This is
removed before conducting our analysis to eliminate the
bias caused by the unrealistic starting state.
Table 1 Scenarios used for capacity planning
Model verification and validation
Input data representing patient classification into stroke
and other conditions were coded and checked separately
by a clinician and a data analyst working on the project.
Data representing arrival rates, length of stay, and pa-
tient routing were screened and analysed by the authors
and then reviewed by experienced stroke pathway staff.
Scenario Description
0. Current admissions Current admission levels; beds are reserved
for either acute or rehab patients
1. 5 % more
admissions
A 5 % increase in admissions across all patient
subgroups.
2. Pooling of acute
and rehab beds
The acute and rehab wards are co-located at
same site. Beds are pooled and can be used
by either acute or rehabilitation patients.
Pooling of the total bed stock of 22 is
compared to the pooling of an increased
bed stock of 26.
3. Partial pooling of
acute and rehab beds
The acute and rehab wards are co-located at
same site. A subset of the 26 beds are pooled
and can be used by either acute or rehab
patients.
4. No complex-
neurological cases
Complex neurological patients are excluded
from the pathway in order to assess their
impact on bed requirements
Monks et al. BMC Health Services Research (2016) 16:530 Page 5 of 8
settings matching recent data gave model predictions
consistent with recent observed system performance.
The programming of the model was verified in two
ways. First, standard testing approaches [32] were applied,
for example extreme value tests for arrival rates for differ-
ent groups of patients entering the model and for patient
routing probabilities. Second, the model underwent peer
review by a specialist researcher who had not been in-
volved in programming the model.
Results
Current and future admissions
The scenarios for current and future admission levels
with different bed capacities are summarised in Table 2
with p(delay) reported to two decimal places. Planning
by average occupancy of the acute unit (9 beds) and
rehabilitation ward (10 beds) leads one in five patients
experiencing a delay in admission. The acute stroke
unit currently has 10 beds (average occupancy plus a
~10 % uplift) with a p(delay) of 0.19 (one in every
seven patients). Even with a ~30 % uplift on average
occupancy (12 beds) it is expected that one in every
16 patients experience a delay. If the number of acute
beds is increased from 10 to 14 (56 % uplift) then
p(delay) falls from 0.14 to 0.02 (1 in every 50 patients),
with diminishing returns for each extra bed.
The 12 bedded rehabilitation ward represents a 20 %
uplift on average occupancy. Transfers and admissions
to rehabilitation have a p(delay) of 0.11 (one in every
nine patients). An increase in rehabilitation beds to 14
Table 2 Likelihood of delay. Current admissions versus 5 %
more admissions
(average occupancy plus a 40 % uplift) would reduce
p(delay) to 0.05 (1 in every 20 patients). A total of 16 re-
habilitation beds (60 % uplift) are required to achieve a
similar p(delay) to 14 acute beds.
An increase of admissions by 5 % in a 14 bed acute
stroke unit increases p(delay) from 0.02 to 0.03 (1 in
every 34 patients). A 14 bed rehabilitation unit would
experience an increase from 0.05 to 0.07 (1 in every 14
patients) while the operation of a 16 bed rehabilitation
unit would be relatively unaffected.
Co-location and bed pooling
We considered two pooling scenarios where the acute
and rehabilitation units are co-located. The first is
complete pooling of the current stock of 22 beds. In the
second we consider the impact of an additional four
beds and the impact of complete pooling versus pooling
of a subset of the 26 beds.
Full pooling of the current bed stock reduces p(delay)
for both acute and rehabilitation patients to 0.06 (1 in
18 patients). If an additional four beds were available
and pooled the likelihood of delays drops to 1 in 64 pa-
tients. Table 3 reports this result along with results from
scenarios where the units are co-located, but only a sub-
set of the 26 beds are pooled (range 0 to 9 beds). This
demonstrates that pooling can be beneficial, but that
there is also a trade-off between acute delays and re-
habilitation delays. As more beds are pooled this trade-
off diminishes.
Effect of complex neurological patients on flow
The final scenario analyses the impact of the complex-
neurological patients on delays in the stroke pathway.
Our hospital manages all complex-neurological patients
in the acute stoke unit (some admitted as suspected
Table 3 Results of pooling of acute and rehab beds
No. acute
beds
Current admissions 5 % more admissions
p(delay)a 1 in every n
patients delayed
p(delay) 1 in every n
patients delayed
9b 0.19 5
10 0.14 7 0.16 6
11 0.09 11 0.11 9
12 0.06 16 0.07 13
13 0.04 28 0.05 21
14 0.02 50 0.03 34
No. rehab
beds
10b 0.20 5
12 0.11 9 0.13 8
13 0.08 13 0.09 11
14 0.05 20 0.07 15
15 0.03 35 0.04 25
16 0.02 57 0.02 42
No. beds P(delay)a 1 in every n
patients
delays
Dedicated
Acute
Dedicated
Rehab
Pooled Acute Rehab Acute Rehab
0 0 22 0.057 0.057 18 18
0 0 26 0.016 0.016 64 64
14 12 0 0.020 0.117 50 9
11 11 4 0.031 0.077 29 13
11 10 5 0.027 0.080 37 12
10 10 6 0.033 0.057 30 17
10 9 7 0.030 0.060 34 17
9 9 8 0.035 0.049 29 20
9 8 9 0.034 0.051 30 20
aP(delay) shown to 2 decimal places only
bAverage occupancy with current admissions rounded to nearest number
of beds
aP(delay) shown to 3 decimal places
Monks et al. BMC Health Services Research (2016) 16:530 Page 6 of 8
stroke) for a short time; however, 11 % of complex-
neurological patients are later transferred and managed
in the community rehabilitation unit. These transferred
patients have an effect on the delays experienced acces-
sing rehabilitation in a 12 bed unit: increasing the num-
ber experiencing delay from 1 in every 17 patients to 1
in every 9. An effect is also seen in the acute stroke with
10 beds with the number experiencing delay increasing
from 1 in every 11 patients to 1 in every 7. To achieve a
0.02 probability of a patient experiencing a delay enter-
ing the acute stroke unit 14 beds are needed with
complex-neurological patients included and 13 without.
A full table of results is provided in the Additional file 1.
Discussion
We emphasise that our model’s utility is in capacity
planning and in particular understanding the trade-off in
the chance of delays under different capacity scenarios.
By design the model is a simplification of the real world
as it allows patients to flow to where they need to go,
and hence estimates‘unfettered’ demand. This simplifi-
cation is at the heart of the models usefulness: it allows
users to understand the actual capacity requirements in
different parts of the pathway.
At our study hospital the model demonstrates that an
increase from 10 to 14 acute stroke unit beds reduces
the number of patients experiencing delays from 1 in
every 7 patients to 1 in every 50. This is a substantial
improvement in smoothing the flow of patients through
the stroke unit and significantly increases the time clini-
cians can focus on patient care as opposed to bed man-
agement. Moreover, the model demonstrates that the
additional four beds is relatively robust to a 5 % increase
in admissions. The modelling also predicts a capacity
shortfall in the inpatient rehabilitation wards. An in-
crease from 12 to at least 14 beds is again required to
smooth the flow and reduce the likelihood of transfer
delays. Obvious extensions to the study are to use the
model to explore the impact of reductions in rehabilita-
tion length of stay that could result from improved dis-
charge planning; reduction in the time to set up a
community care package (reductions in‘bed blocking’);
or extending the capacity of ESD services to care for
more severely affected patients– potential greatly redu-
cing length of stay [16].
The study hospital was also planning to co-locate the
acute stroke unit and rehabilitation wards. Even if bed
pooling between the two units is not officially sanc-
tioned, in practice it is likely that some temporary bed
pooling will happen in order to cope with the spontan-
eous variation in rates of patient admissions and dis-
charges. The model therefore provides a prospective way
to plan the implementation of bed pooling and to fully
understand the trade-offs when pooling only a subset of
beds.
The model was also used to analyse the impact of
complex-neurological patients on flow through the path-
way. The utility of such information is in the dialog be-
tween clinicians and healthcare commissioners to
understand the implications of service provision to dif-
ferent patient subgroups on overall performance.
There are several further ways in which our model can
be used, depending on the issues seen to be important
in different contexts. For example, it could be used to
explore scenarios where stroke beds are reserved exclu-
sively for patients suffering an acute stroke (so called
‘ring-fencing’), or‘partial ring-fencing’ in which admis-
sions of other cases is dependent on ward occupancy.
The unfettered demand approach used in our model is
generalizable and hence is applicable to other relevant
wards. For example, a second use for our model would
be to adapt it for other hospital wards, such as those for
the cardiac surgery, where timely admission and dis-
charge are important.
The strengths of our approach to capacity planning
are threefold. First, the model provides a sophisticated
analysis of capacity requirements accounting for the
spontaneous and unpredictable variability in patient ar-
rivals and lengths of stay. This level of detail is often
missing from capacity calculations. Planning models that
rely on average occupancy only will greatly underesti-
mate bed requirements as they take insufficient account
of variability. In this study average occupancy of the 10-
bedded acute stroke unit was nine patients, correspond-
ing to delays for one in every five patients. Our study
provides a scientific methodology for analysing how
many beds above average occupancy are necessary in
order to limit the probability of delay. Second, although
sophisticated, the model is driven by routinely collected
data that is readily available from patient administration
systems. Last, as the planning model has no capacity
constraints, it is not necessary to model what happens to
patients when stroke wards are full. Its independence of
these details, which can vary considerably across hospi-
tals, greatly increases the applicability of the model to
other settings.
When adapting our model for similar studies, model-
lers may face the issue of dealing with the impact of
‘bed blocking’ increasing the lengths of stay recorded in
routinely collected data. That is, the length of stay data
do not separate treatment duration and transfer/dis-
charge delays. If sensitivity analyses show that these dis-
crepancies are likely to cause misleading results, a small
prospective sample of times where patients are fit for
transfer to rehabilitation versus when they are trans-
ferred, or a historic sample of lengths of stay during pe-
riods of time when beds are not blocked can be used.
Monks et al. BMC Health Services Research (2016) 16:530 As our model focuses on capacity requirements, a
limitation is that it cannot predict the length of a delay
that a patient experiences. This means that the model
cannot be used to investigate performance metrics such
as the UK’s four hour stroke unit target or the propor-
tion of patients that spend 90 % of their stay on a stroke
unit. Although creation of such models is possible the
complexity increases by several orders of magnitude and
will inevitably require data that is not routinely collected
– for example regarding the management and repatri-
ation of outlying stroke patients. The exclusion of such
measures not only reduces our model’s data require-
ments, but also makes our approach more general inter-
nationally (where targets such as the 90 % stay metric do
not apply). The model is easily adaptable to other acute
stroke units which transfer patients to multiple inpatient
rehabilitation wards in the community and could be
used to explore the impact of introducing new cost ef-
fective services such as ESD [33].
The simulation-based method used here was chosen in
preference to attempting to derive heuristics based on
queueing theory for calculating the uplifts to associate
with different occupancy levels as a more direct way to
incorporate the characteristics of the particular problem.
However, the simulation model development was guided
by a knowledge of relevant queueing theories, in the
spirit of complementary use of simulation and queueing
theory [34].
Conclusions
Planning by average occupancy plus an arbitrary uplift,
even up to 30-40 %, fails to provide sufficient reserve
capacity to adequately manage the variation in admission
and discharges seen in our stroke pathway. Our method
draws on long available, intuitive, but underused math-
ematical techniques for capacity planning. Implementa-
tion via simulation at our study hospital provided
valuable decision support for planners to assess future
bed numbers and organisation of the acute and rehabili-
tation services.
In recent years some aspects of stroke services have
been modelled using discrete-event simulation ap-
proaches, [8, 19–25] including access to time-sensitive
treatments such as thrombolysis. Our method, with its
focus on capacity, is complementary to these models
and will be particularly useful for cases of stroke service
reconfigurations where acute stroke units will face sub-
stantially increased admissions, including patients for
whom the final diagnosis is not stroke. To enable cost-
effective and efficient provision planning decisions in
such complex systems requires all of the relevant infor-
mation to be considered in a way that is not possible for
simple average-based estimates. Our method accounts
for the variation in admission patterns, length of stay by
Page 7 of 8
patient type and eligibility for ESD, greatly increasing
the precision with which services can be planned and
the ability to predict and respond to short and long-
term variation in demand for emergency stroke services.
Additional file
Additional file 1: Supplementary methodology and results. (DOCX 28 kb)
Abbreviations
ED: Emergency department; ESD: Early supported discharge; p(delay): The
probability of a delay; PDF: Probability density function; TIA: Transient
Ischemic Attack
Acknowledgements
None.
Funding
This article presents independent research funded by the National Institute
for Health Research (NIHR) Collaboration for Leadership in Applied Health
Research and Care (CLAHRC) South West Peninsula. TM is funded by NIHR
CLAHRC Wessex. The views expressed in this publication are those of the
author(s) and not necessarily those of the National Health Service, the NIHR,
or the Department of Health.
Availability of data and materials
The model is highly generalizable to other stroke pathways. Specific results
can be recreated as follows. Model logic and arrival rates for patient classes
are detailed in the main text. For length of stay distributions and patient
routing see the online Additional file 1. The model has a run length of
5 years. A warm-up period of 3 years was used with 150 replications.
Authors’ contribution
TM designed the study, performed the analysis and wrote the paper. DW
designed the study, oversaw the analysis and contributed to writing the
paper. MA, MP and KS provided input to the methodology and commented
on drafts of the paper. MJ provided clinical guidance and oversight and
contributed to writing the paper. All authors have read and approved the
final manuscript.
Competing interests
The authors declare that they have no competing interests.
Consent for publication
Not applicable.
Ethics approval and consent to participate
This publication presents the results of a service evaluation project
conducted in collaboration with an NHS Trust in the UK using routinely
collected administrative data only, and thus did not require ethical approval
or individual participant consent. No patients were involved or identified, no
new data were generated or collected, and no care pathways were altered.
Author details
1NIHR CLAHRC Wessex, Faculty of Health Sciences, University of
Southampton, Southampton SO17 1BJ, UK. 2Lancaster University
Management School, Lancaster University, Lancaster LA1 4YX, UK. 3NIHR
CLAHRC South West Peninsula, University of Exeter Medical School,
University of Exeter, Exeter EX1 2LU, UK.
Received: 13 August 2016 Accepted: 23 September 2016
References
1. Pitt M, Monks T, Allen M. Systems modelling for improving healthcare. In:
Richards D, Rahm Hallberg I, editors. Complex interventions in health: an
overview of research methods. London: Routledge; 2015.
Monks et al. BMC Health Services Research (2016) 16:530 Page 8 of 8
2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. Brailsford SC, Harper PR, Patel B, Pitt M. An analysis of the academic literature
on simulation and modelling in health care. J Simul. 2009;3(3):130–40.
Fone D, et al. Systematic review of the use and value of computer
simulation modelling in population health and health care delivery. J Public
Health. 2003;25(4):325–35. doi:10.1093/pubmed/fdg075.
Atkinson J-A, Page A, Wells R, Milat A, Wilson A. A modelling tool for policy
analysis to support the design of efficient and effective policy responses for
complex public health problems. Implement Sci. 2015;10(1):26.
Gallivan S, Utley M, Treasure T, Valencia O. Booked inpatient admissions and
hospital capacity: mathematical modelling study. BMJ. 2002;324(7332):280–2.
doi:10.1136/bmj.324.7332.280.
Utley M, Gallivan S, Treasure T, Valencia O. Analytical methods for calculating
the capacity required to operate an effective booked admissions policy for
elective inpatient services. Health Care Managment Science. 2003;6(2):97–104.
doi:10.1023/A:1023333002675.
Günal MM, Pidd M. Understanding target-driven action in emergency
department performance using simulation. Emerg Med J. 2009;26(10):724–7.
doi:10.1136/emj.2008.066969.
McClean S, Barton M, Garg L, Fullerton K. A modeling framework that combines
markov models and discrete-event simulation for stroke patient care. ACM Trans
Model Comput Simul. 2011;21(4):1–26. doi:10.1145/2000494.2000498.
Bayer S, Petsoulas C, Cox B, Honeyman A, Barlow J. Facilitating stroke care
planning through simulation modelling. Health Informatics J. 2010;16(2):129–43.
Hunter RM, et al. Impact on clinical and cost outcomes of a centralized approach
to acute stroke care in London: a comparative effectiveness before and after
model. PLoS ONE. 2013;8(8):e70420. doi:10.1371/journal.pone.0070420.
Morris S. et al.. Impact of centralising acute stroke services in English
metropolitan areas on mortality and length of hospital stay: difference-in-
differences analysis. BMJ. 2014. 349. doi:10.1136/bmj.g4757.
Monks T, Pitt M, Stein K, James M A. Hyperacute stroke care and NHS
England’s business plan. BMJ. 2014. 348. doi: 10.1136/bmj.g3049.
NHS England. NHS England’s business plan 2014/15–2016/17: Putting
Patients First. 2014.
Bagust A, Place M, Posnett JW. Dynamics of bed use in accommodating
emergency admissions: stochastic simulation model. BMJ. 1999;319(7203):
155–8. doi:10.1136/bmj.319.7203.155.
Lynch E, Hillier S, Cadilhac D. When should physical rehabilitation
commence after stroke: a systematic review. Int J Stroke. 2014;9(4):468–78.
doi:10.1111/ijs.12262.
Fearon P, Langhorne P. Services for reducing duration of hospital care for
acute stroke patients. Cochrane Database Syst Rev. 2012;9:Cd000443. doi:10.
1002/14651858.CD000443.pub3.
Fisher RJ, et al. A consensus on stroke: early supported discharge. Stroke.
2011;42(5):1392–7. doi:10.1161/strokeaha.110.606285.
Corporation S. Simul8. 2015 01/04/2016; Available from: www.Simul8.com.
Accessed 27 Sept 2016.
Churilov L, Donnan GA. Operations research for stroke care systems: an
opportunity for the science of better to do much better. Oper Res Health
Care. 2012;1(1):6–15. doi:10.1016/j.orhc.2011.12.001.
Churilov L, Fridriksdottir A, Keshtkaran M, Mosley I, Flitman A, Dewey HM.
Decision support in pre-hospital stroke care operations: a case of using
simulation to improve eligibility of acute stroke patients for thrombolysis
treatment. Comput Oper Res. 2013;40(9):2208–18. http://dx.doi.org/10.1016/j.
cor.2012.06.012.
Cordeaux C, Hughes A, Elder M. Simulating the impact of change:
implementing best practice in stroke care. London J Primacy Care. 2011;4:33–7.
Lahr MMH, van der Zee D-J, Luijckx G-J, Vroomen PCAJ, Buskens E. A
simulation-based approach for improving utilization of thrombolysis in
acute brain infarction. Med Care. 2013;51(12):1101–5. doi:10.1097/MLR.
0b013e3182a3e505.
Lahr MMH, van der Zee D-J, Luijckx G-J, Vroomen PCAJ, Buskens E.
Thrombolysis in acute ischemic stroke: a simulation study to improve pre-
and in-hospital delays in community hospitals. PLoS ONE. 2013. doi:10.1371/
journal.pone.0079049.
Monks T, Pitt M, Stein K, James M. Maximizing the population benefit from
thrombolysis in acute ischemic stroke: a modeling study of in-hospital
delays. Stroke. 2012;43(10):2706–11. doi:10.1161/strokeaha.112.663187.
Pitt M, Monks T, Agarwal P, Worthington D, Ford GA, Lees KR, Stein K, James
MA. Will delays in treatment jeopardize the population benefit from
extending the time window for stroke thrombolysis? Stroke. 2012;43(11):
2992–7. doi:10.1161/strokeaha.111.638650.