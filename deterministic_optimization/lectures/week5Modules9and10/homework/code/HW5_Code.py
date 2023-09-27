# IMPORTS
import numpy as np
import cvxpy as cp
import math as m

# QUESTION 1
print("------------QUESTION 1-----------")

'''
In .docx
'''

# QUESTION 2
print("\n------------QUESTION 2-----------")
'''
for each starting point, print out the step length ak and point xk for every step k.
Newton's Method should converge very fast.
'''
x, x_later = np.matrix([1.2, 1.2]), np.matrix([-1.2, 1])

def f(x):

    x1 = x[0,0]
    x2 = x[0, 1]
    
    return 100 * (x2 - x1**2)**2 + (1 - x1)**2

def fprime(x):

    x1 = x[0,0]
    x2 = x[0, 1]

    df_dx1 = (-400 * x1 * x2) + (400 * x1**3) - 2 + (2 * x1)    
    df_dx2 = (200 * x2) - (200*x1**2)

    return np.matrix([[df_dx1], [df_dx2]])

def f_doubleprime(x):

    x1 = x[0,0]
    x2 = x[0, 1]
    
    dfx1_dx1 = -400 * x2 + 1200 * x1**2 + 2
    dfx1_dx2 = -400 * x1
    dfx2_dx1 = -400 * x1 
    dfx2_dx2 = 200
    
    return np.matrix([[dfx1_dx1, dfx1_dx2],
                    [dfx2_dx1, dfx2_dx2]])

def dk_cal(xk):

    return -np.linalg.inv(f_doubleprime(xk)) @ fprime(xk)

def left_right(xk, alphak, dk, c):
    
    left_side = f(xk + alphak * dk.T)
    right_side = f(xk) + (c * alphak * fprime(xk)).T @ dk

    return left_side > right_side    

def newtons_method_line_search(xk):
    
    # set
    k = 0
    eps = m.pow(10, -4)
    dk = dk_cal(xk)
    d = {}
    
    while np.linalg.norm(fprime(xk)) > eps:
        # choose alpha, row, and c
        row = 0.5
        c = 0.5
        abar = 1
        alphak = abar
        while left_right(xk, alphak, dk, c):
            
            alphak = row * alphak
            
        xk = xk + alphak * dk.T
        dk = dk_cal(xk)
        d[k] = [xk, alphak]
        print(f'{xk=} {alphak=} {k=}')
        k += 1
        
    return d

print(f"\n{x=}")
newtons_method_line_search(x)
print(f"\n{x_later=}")
newtons_method_line_search(x_later)

# QUESTION 3
print("\n------------QUESTION 3-----------")
'''
This is written in my notebook
'''

# QUESTION 4
print("\n------------QUESTION 4-----------")

# COSTS
# demand
d = np.array([100,  65, 95])

# unit generation costs
c = np.array([16, 20, 8])

# CONSTRAINTS
# generator production upper/lower bounds
p_min = np.array([20, 20, 10])
p_max = np.array([200, 150, 150])

# flow limits
f12_min, f12_max = -100, 100
f23_min, f23_max = -110, 110
f34_min, f34_max = -50, 50
f45_min, f45_max = -80, 80
f56_min, f56_max = -60, 60
f61_min, f61_max = -40, 40

# branch flow
b = np.array([11.6, 5.9, 13.7, 9.8, 5.6, 10.5])

# PART A
print("---------------------PART A---------------------")
'''
This is written in my notebook.
'''

# PART B
print("\n---------------------PART B---------------------")
f12 = cp.Variable(1)
f23 = cp.Variable(1)
f34 = cp.Variable(1)
f45 = cp.Variable(1)
f56 = cp.Variable(1)
f61 = cp.Variable(1)

p1 = f12 - f61
p2 = f34 - f23
p3 = f56 - f45

theta1 = cp.Variable(1)
theta2 = cp.Variable(1)
theta3 = cp.Variable(1)
theta4 = cp.Variable(1)
theta5 = cp.Variable(1)
theta6 = cp.Variable(1)

p = cp.hstack([p1, p2, p3])

expr = cp.sum(cp.multiply(c, p))
obj = cp.Minimize(expr)

constraints = [p >= p_min, 
               p <= p_max,
               f12 >= f12_min,
               f12 <= f12_max,
               f23 >= f23_min,
               f23 <= f23_max,
               f34 >= f34_min,
               f34 <= f34_max,
               f45 >= f45_min,
               f45 <= f45_max,
               f56 >= f56_min,
               f56 <= f56_max,
               f61 >= f61_min,
               f61 <= f61_max,
               -d[0] == f23 - f12,
               -d[1] == f45 - f34,
               -d[2] == f61 - f56,
               f12 == b[0] * (theta1 - theta2),
               f23 == b[1] * (theta2 - theta3),
               f34 == b[2] * (theta3 - theta4),
               f45 == b[3] * (theta4 - theta5),
               f56 == b[4] * (theta5 - theta6),
               f61 == b[5] * (theta6 - theta1)]

electric = cp.Problem(obj, constraints)
electric.solve()
print("\nThe optimal value is", round(electric.value, 2))

# PART C
print("\n---------------------PART C---------------------")
for i in range(14, 17):
    print(f"The dual value for the {i} constraint: ${round(constraints[i].dual_value[0], 2)}")

for i in [p1, p2, p3, f12, f23, f34, f45, f56, f61, theta1, theta2, theta3,theta4, theta5,theta6]:
    print(f"{i[0].value=}")