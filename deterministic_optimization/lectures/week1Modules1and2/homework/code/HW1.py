# IMPORTS
import pandas as pd
import numpy as np
from cvxpy import *
import matplotlib.pyplot as plt
from scipy.optimize import fmin
from mpl_toolkits.mplot3d import axes3d

# QUESTION 1 - COMPLETE
print("------------QUESTION 1-----------")
'''x, y = (-1, 0), (0, -1) (-0.5, -0.5), 
f(x, y) = 5, 5, 4.5
'''

# THIS CODE SHOWS THE ABOVE MAXES FOR X. THE Y CAN BE INFERRED USING SOME QUICK MATH
# THE DESMOS PLOT IS BETTER
fig, ax = plt.subplots(figsize=(6, 6))
X = np.linspace(-1, 1)
Y = np.linspace(-1, 1)
z1 = [(x, y) for x in X for y in Y if np.abs(x) + np.abs(y) <= 1] 
z2 = [(x - 1)**2 + (y - 1)**2 for x, y in z1]
X = [x for x in X for y in Y if np.abs(x) + np.abs(y) <= 1]

plt.plot(X, z2)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 6)

plt.show()

# QUESTION 2 - COMPLETE
print("\n------------QUESTION 2-----------")
# SEE NOTEBOOK FOR THE ACTUAL CALCULUS OR WRITE HERE.
"""x = 1/6; f(x) = 2/27"""

fig, ax = plt.subplots(figsize=(6, 6))
X = np.linspace(0, 0.5)
y = [x * (1-2*x) ** 2 for x in X]
plt.plot(X, y)
ax.annotate('Maximum (x=1/6, f(x) = 2/27)',
            xy=(1/6, 2/27), xycoords='data',
            xytext=(0.50, 0.70), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.03),
            horizontalalignment='right', verticalalignment='top')
ax.set_xlim(0, 0.6)
ax.set_ylim(0, 0.2)

plt.show()

# QUESTION 3
print("\n------------QUESTION 3-----------")
# A) - COMPLETE
print("***PART A***")
print("Mixed Integer Quadratic; Mixed Integer Nonlinear ")

# B) - COMPLETE
print("\n***PART B***")
"-min{-xy**2 + xz**2}"

# C)
print("\n***PART C***")
'''x, y, z = 1, 1, 0 => f(x, y, z) = 1
   x, y, z = 1, -1, 0 => f(x, y, z) = 1'''

# QUESTION 4 - COMPLETE
print("\n------------QUESTION 4-----------")
"""NOTE: PER THE HOMEWORK DIRECTIONS, ALL OF THE BELOW CODE HAS BEEN BORROWED FROM MODULE 2 LESSON 3
AND FILE portopt_cvxpy_python3.py

RESULTS FROM MODULE 2 LESSON 3:
MSFT: Exp ret = 0.024611, Risk = 0.058040
V: Exp ret = 0.018237, Risk = 0.042807
WMT: Exp ret = 0.009066, Risk = 0.044461
----------------------
Optimal portfolio
----------------------
x[MSFT] = 0.100500
x[V] = 0.414335
x[WMT] = 0.485165
----------------------
Exp ret = 0.014428
risk    = 0.025495
----------------------

RESULTS FROM HOMEWORK:
MSFT: Exp ret = 0.009017, Risk = 0.074529
V: Exp ret = 0.006443, Risk = 0.069428
WMT: Exp ret = 0.008314, Risk = 0.061025
----------------------
Optimal portfolio
----------------------
x[MSFT] = 0.253497
x[V] = 0.310816
x[WMT] = 0.435688
----------------------
Exp ret = 0.007910
risk    = 0.053730
----------------------

COMPARE AND CONTRAST:
With the new data and after optimization:
MSFT gets a higher investment with new data
V gets a lower investment with new data
WMT gets a lower investment with new data
Expected Returns are lower with new data
Risk is higher with new data
"""

# read monthly_prices.csv
mp = pd.read_csv("monthly_prices.csv",index_col=0)
mr = pd.DataFrame()

# compute monthly returns
for s in mp.columns:
    date = mp.index[0]
    pr0 = mp[s][date] 
    for t in range(1,len(mp.index)):
        date = mp.index[t]
        pr1 = mp[s][date]
        ret = (pr1-pr0)/pr0
        #mr.set_value(date,s,ret)
        mr.at[date,s]=ret
        pr0 = pr1
        
# get symbol names
symbols = mr.columns

# convert monthly return data frame to a numpy matrix
#return_data = mr.as_matrix().T
return_data = mr.values.T

# compute mean return
r = np.asarray(np.mean(return_data, axis=1))

# covariance
C = np.asmatrix(np.cov(return_data))

# print out expected return and std deviation
print("----------------------")
for j in range(len(symbols)):
    print('%s: Exp ret = %f, Risk = %f' %(symbols[j],r[j], C[j,j]**0.5))
   

# set up optimization model
n = len(symbols)
x = Variable(n)
req_return = 0.006
ret = r.T@x
risk = quad_form(x, C)
prob = Problem(Minimize(risk), 
               [sum(x) == 1, ret >= req_return, x >= 0])

# solve problem and write solution
try:
    prob.solve()
    print("----------------------")
    print("Optimal portfolio")
    print("----------------------")
    for s in range(len(symbols)):
        #print('x[%s] = %f'%(symbols[s],x.value[s,0]))
        print('x[%s] = %f'%(symbols[s],x.value[s]))
    print("----------------------")
    print('Exp ret = %f' %(ret.value))
    print('risk    = %f' %((risk.value)**0.5))
    print("----------------------")
except:
    print('Error')
