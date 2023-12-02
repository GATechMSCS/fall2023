# IMPORTS
import math as m
from  scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt

# QUESTION 1
print("------------QUESTION 1-----------")

# A)
print("***PART A***")
'''Find the probability that abs(x) < 0.5'''

x = .5
print(x**(3/16) - -x**(3/16))

# B)
print("\n***PART B***")
'''In .docx'''

# C)
print("\n***PART C***")
'''In .docx'''

# D)
print("\n***PART D***")
'''In .docx'''

# QUESTION 2
print("\n------------QUESTION 2-----------")
'''
System is operational if k out of n components are operational
Assume: n = 8, k = 5, r = 3/2, lambda = 1/10
t = months, lambda = inverse months, r is dimensionless
For each component the probability of the system working at time t is p = e**((-0.1)*(t**3/2)) for t >= 0
'''

# A)
print("***PART A***")
n = 8
k = 5
r = 3/2
lmbda = 1/10
t = 3
e = m.e

prob_each_comp = (e**((-lmbda)*(t**r)))
operational = binom.cdf(k - 1, n, prob_each_comp)
print(f"Probability at 3 months that the system will be operational: {1 - operational}")
'''
ANSWER: 0.5818670523703137
'''

# B)
print("\n***PART B***")
'''
Given the system is operational, what is the probability that exactly five components were operational?
'''

Pba = 1.0
Pb = operational
Pa = binom.pmf(5, 8, prob_each_comp)

def bayes(Pba, Pa, Pbna=None, Pna=None, Pb=None):
    # P(A | B) = (P(B | A) * P(A)) / P(B)
    
    if not Pb:
        Pb = (Pa * Pba) + (Pna * Pbna)
    return (Pba * Pa) / Pb

exactly_five = bayes(Pba=Pba, Pa=Pa, Pb=Pb)
print(f"Given the system is operational, the probability that exactly five components were operational: {exactly_five}")

'''
ANSWER: 0.663307140632011
'''

# QUESTION 3
print("\n------------QUESTION 3-----------")
'''
firing times are defined as time instances when a neuron sends a signal to another linked neuron (a spike).
rat brain cells cultureed for 18 days and stimulated at the rate of 1 Hz.
MLE - Maximum Likelihood Estimation
'''
neuron = pd.read_excel(io='neurondiffs.xlsx', header=None, names=['firing_times'])['firing_times']

# A)
print("\n***PART A***")
neuron.hist(bins=10)
plt.show()

'''
It's a right-tailed histogram which is high on left and drops to be low on the right. This is a similar concept to the exponential density graph.

'''
n = 988
x_i = neuron.sum()
lam_MLE = n / x_i
print(lam_MLE)

'''
ANSWER: 0.9900623989833222
'''

# B)
print("\n***PART B***")
'''Find the posterior distribution of the lambda when the prior is gamma (18, 20)'''
alpha = 18
beta = 20
new_alpha = alpha + n
new_beta = x_i + beta
lam = 1 / new_beta
likelihood = lam**(new_alpha - 1)
gamma = m.e**(-lam * new_beta)
posterior = likelihood * gamma

print(posterior)

'''What is the Bayes estimator for lambda?'''
bayes_estimator = new_alpha / new_beta
print(bayes_estimator)

'''
ANSWER: 0.9882928557331153
'''

'''Find also the posterior variance of lambda'''
variance = new_alpha / (new_beta**2)
print(variance)

'''
ANSWER: 0.0009708973843867955
'''

# C)
print("\n***PART C***")
inverse_alpha = 18
inverse_beta = 20
newinverse_alpha = inverse_alpha + n
newinverse_beta = inverse_beta + x_i
post_mean = newinverse_beta / (newinverse_alpha - 1)
post_var = (newinverse_beta**2) / (((newinverse_alpha - 1)**2) * (newinverse_alpha - 2))

print(post_mean, post_var)

# D)
print("\n***PART D***")

'''
True
'''
