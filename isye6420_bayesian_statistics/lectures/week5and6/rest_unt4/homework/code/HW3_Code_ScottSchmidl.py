# IMPORTS
import math as m
import sympy as sp
import numpy as np
from scipy.optimize import fsolve
from scipy.special import gamma as gamma_func
from scipy.stats import gamma, expon, norm
from tqdm.auto import tqdm
import arviz as az

# QUESTION 1
print("------------QUESTION 1-----------")
'''
Bayes Estimator
'''
# A)
print("***PART A***")
n = 4

'''What is the Bayes estimator for lambda?'''
alpha = 5.5
beta = 4
bayes_estimator = alpha / beta
print(bayes_estimator)

'''MLE'''
sum_x = sum(1,2,2,0)
mle = sum_x / n

# B)
print("\n***PART B***")
'''
code borrowed directly from lecture TA jupyter nb
'''
a = 5.5
b = 4
n = 1000000
samples = gamma.rvs(a, scale=1 / b, size=n)

x = np.sort(samples)
alpha = 0.05

lower_idx = int(np.floor(alpha / 2 * n))
upper_idx = int(np.floor((1 - alpha / 2) * n))

print(f"manual = {x[lower_idx], x[upper_idx]}")

np.quantile(samples, (0.025, 0.975))

# C)
print("\n***PART C***")
'''
code borrowed directly from lecture TA jupyter nb
'''
def calc_hdi(samples: np.ndarray, alpha: float = 0.05) -> tuple:
    n = len(samples)
    x = np.sort(samples)

    lower_idx = int(np.floor(alpha * n))
    x_left = x[:lower_idx]
    x_right = x[n - lower_idx :]

    idx = np.argmin(x_right - x_left)

    upper_bound = x_right[idx]
    lower_bound = x_left[idx]

    return lower_bound, upper_bound


a = 5.5
b = 4
samples = gamma.rvs(a, scale=1 / b, size=1000000)
lower, upper = calc_hdi(samples, alpha=0.05)

prob = gamma.cdf(upper, a, scale=1 / b) - gamma.cdf(lower, a, scale=1 / b)
print(f"HPD credible set: {lower, upper}")
print(f"length = {upper - lower}")
print(f"probability within these bounds: {prob}")
fsolve(conditions, (guess_lwr, guess_upr))

# D)
print("\n***PART D***")

# E)
print("\n***PART E***")


# QUESTION 2
print("\n------------QUESTION 2-----------")
'''

'''
x, a, e, pi = sp.symbols('x a e pi')
sp.init_printing(use_unicode=True)

expr = (3/2) * sp.ln(a) - (a*(x**2))/2

first_d = sp.diff(expr, a)
#print(sp.latex(first_d))

second_d = sp.diff(first_d, a)
#print(sp.latex(second_d))

maxwell = (sp.sqrt(2/pi)) * a**(3/2) * x**2 * e**(-a * x**2)
#print(sp.latex(maxwell))

integrate_expr = second_d * maxwell
expected = sp.integrate(integrate_expr, a)
#print(sp.latex(expected))

neg_expected = -expected
root_neg_expect = sp.sqrt(neg_expected)
#print(sp.latex(root_neg_expect))

# QUESTION 3
print("\n------------QUESTION 3-----------")
'''

'''
theta, a, e, y = sp.symbols('theta a e y')
sp.init_printing(use_unicode=True)

expr = theta**(-a- 1) * e**((1/theta) * (y + 1))
print(sp.latex(expr))

bayes = sp.integrate(expr, theta)
#print(sp.latex(expected))
