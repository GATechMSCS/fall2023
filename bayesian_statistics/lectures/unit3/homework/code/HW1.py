# IMPORTS
import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import CausalInference
from pgmpy.models import BayesianNetwork

# Question 1
print("------------QUESTION 1-----------")
'''BayesNetwork:
After the semester Chad is in Coco Beach. Given that Chad is in Coco Beach, what is the probability that Chad got a car?'''

prob_a = 0.7
prob_notA = 0.3
prob_car_given_a = 0.9
prob_car_not_a = 0.1
prob_cocoBeach_given_car = 0.7
prob_stayCampus_given_car = 0.3
prob_cocoBeach_not_car = 0.2
prob_stayCampus_not_car = 0.8

# SETUP NETWORK
grade_model = BayesianNetwork(
    [("A", "Car"),
     ("Car", "Coco Beach"),
     ("Car", "Campus"),])

# PARAMETERS FOR MODEL
cpd_A = TabularCPD(
    variable="A",
    variable_card=2,
    values=[[prob_a],
            [prob_notA]])

cpd_car = TabularCPD(
    variable="Car",
    variable_card=2,
    values=[[prob_car_given_a, 0.1],
            [prob_car_not_a, 0.9]],
    evidence=["A"],
    evidence_card=[2],)

cpd_beach = TabularCPD(
    variable="Coco Beach",
    variable_card=2,
    values=[[prob_cocoBeach_given_car, 0.2],
            [0.3, 0.8]],
    evidence=["Car"],
    evidence_card=[2],)

cpd_campus = TabularCPD(
    variable="Campus",
    variable_card=2,
    values=[[prob_stayCampus_given_car, 0.8],
            [0.7, 0.2]],
    evidence=["Car"],
    evidence_card=[2],)

# ADD PARAETERS TO MODEL
grade_model.add_cpds(cpd_A,
                     cpd_car,
                     cpd_beach,
                     cpd_campus,)

grade_model.check_model()

print(f"Nodes: {grade_model.nodes()}")
print(f"Edges: {grade_model.edges()}")

options = {
    "arrowsize": 40,
    "font_size": 8,
    "font_weight": "bold",
    "node_size": 4000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 5,
    "alpha": 0.9,}

nx.draw_circular(grade_model, with_labels=True, **options)

# PLOTTING
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

# INFERENCE
grade_infer = CausalInference(grade_model)

# PROB CHAD GOT AN A GIVEN HE'S IN COCO BEACH
q = grade_infer.query(variables=["A"],
                      evidence={"Coco Beach": True})
print("P(cb|a)")
print(q)

# Answer:
'''The probablility is 0.5213'''

# Question 2
print("\n------------QUESTION 2-----------")
#Tinel’s sign Sensitivty 
ts_sens_tp = 0.98
ts_sens_fn = 0.02

#Tinel’s sign Specificity
ts_spec_tn = 0.91
ts_spec_fp = 0.09

# Phalen’s test Sensitivity
pt_sens_tp = 0.92
pt_sens_fn = 0.08

# Phalen’s test Specificity
pt_spec_tn = 0.88
pt_spec_fp = 0.12

# nerve conduction velocity test Sensitivity
nerve_cond_vel_sens_tp = 0.93
nerve_cond_vel_sens_fn = 0.07

# nerve conduction velocity test Specificity
nerve_cond_vel_spec_tn = 0.87
nerve_cond_vel_spec_fp = 0.13

''' Tests are conditionally independent.
Calculate the sensitivity and specificity of a combined test if combining is done.

Sensitivity = TP / (TP + FN) = TP / nD
nD = Total number with disease present (TP + FN)

Specificity = TN / (FP + TN) = TN / nC
nC = Total number without disease present (TN + FP) 

Prevalence = (TP + FN) / (TP + FP + FN + TN) = nD / n
nD = Total number with disease present (TP + FN)
n = Total sample size (TP + FP + FN + TN)

Positive Predictive Value (PPV) = TP / (TP + FP) = TP/ nP
nP = Total number of positives (TP + FP)'''

def combined_sensitivity(test_se: list[float], manner: str) -> float:

    sensitivity = 1
    if manner == 'serial':
        
        for s in test_se:
            sensitivity *= s
        
    else:

        for s in test_se:
            sensitivity *= 1 - s

        sensitivity = 1 - sensitivity
            
    return sensitivity

def combined_specificity(test_sp: list[float], manner: str) -> float:
    
    specificity = 1
    
    if manner == 'serial':
        
        for s in test_sp:
            specificity *=  1 - s

        specificity = 1 - specificity
        
    else:

        for s in test_sp:
            specificity *= s
    
    return specificity

test_se = [ts_sens_tp, pt_sens_tp, nerve_cond_vel_sens_tp]
test_sp = [ts_spec_tn, pt_spec_tn, nerve_cond_vel_spec_tn]

def positive_predicted_value(se:float, sp:float, pre:float=50/1000) -> float:

    return (se * pre) / se * pre + (1 - sp) * (1 - pre)

# A)
'''Serial Manner?
Se = Se_1 x Se_2 ...Se_k
Sp = 1 - [(1 - Sp_1) x (1 - Sp2) ... (1 - Sp_k])'''

print("***PART A***")
print(f"Combined Sensitivity for Serial: {combined_sensitivity(test_se, 'serial')}")
print(f"Combined Specificity for Serial: {combined_specificity(test_sp, 'serial')}")

# B)
'''Parallel Manner?
Se = 1 - [(1 - Se_1) X (1 - Se_2) ... (1 - Se_k)]
Sp = Sp_1 X Sp_2 ... Sp_k'''

print("\n***PART B***")
print(f"Combined Sensitivity for Parllel: {combined_sensitivity(test_se, 'parallel')}")
print(f"Combined Specificity for Parllel: {combined_specificity(test_sp, 'parallel')}")

# C)
'''Positive Predictive Value for tests (a) and (b),
if the prevalence of carpal tunnel syndrome in the general population is approximately 50 cases per 1000 subjects (50/1000)?'''

print("\n***PART C***")
se_serial = combined_sensitivity(test_se, 'serial')
sp_serial = combined_specificity(test_sp, 'serial')
print(f"Combined Positive Predicited Value for serial: {positive_predicted_value(se=se_serial, sp=sp_serial)}")

se_parallel = combined_sensitivity(test_se, 'parallel')
sp_parallel = combined_specificity(test_sp, 'parallel')
print(f"Combined Positive Predicited Value for parallel: {positive_predicted_value(se=se_parallel, sp=sp_parallel)}")

# Question 3
print("\n------------QUESTION 3-----------")
'''
1) student answers multiple choice exam with 2qs that have 4 choices each.
5) questions are independent
'''
prob_knows = 0.70
prob_guesses = 0.30
prob_guess_correct = 0.25

# A)
print("\n***PART A***")
'''what is prob that both questions will be answered correctly?
'''
prob_1_correct = prob_knows + (prob_guesses * prob_guess_correct)
prob_2_correct = prob_1_correct**2
print(prob_2_correct)

# B)
print("\n***PART B***")
'''if answered correctly, what is prob that student really new the correct answer to both questions?
p(knew correct answer | answered correct)
A - answer correct both times
H1 - guessed answer
H2 =  knew answer
'''
h1 = 0.3
h2 = 0.7
A = prob_2_correct
p_A_h1 =  (prob_guesses * prob_guess_correct) ** 2
p_A_h2 = prob_knows ** 2

p_h2_A = (h2 * p_A_h2) / (A)
print(p_h2_A)

# C)
print("\n***PART C***")
'''how would you generalize above from 2 to n questions?
that is, what are answers to (a) and (b) if the test has n independent questions?
what happens to prob's in (a) and (b) if n > inf?
A - get n questions correct
H1 = guessed answer
H2 = knew answer
'''

# GENERAL FORUMLA
for n in range(1, 10):
    new_p_A_h2 = prob_knows ** n
    new_p_h2_A = (h2 * new_p_A_h2) / (prob_knows + (prob_guesses * prob_guess_correct)) ** 2
    print(new_p_h2_A)

# WHAT HAPPENS TO PROBABILITIES IN THIS CASE?
'''The probabilities go down, because it becomes less and less probable that you know every answer'''    

