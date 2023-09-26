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
x, x_later = np.array([1.2, 1.2]), np.array([-1.2, 1])

def f(x):

    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def fprime(x):
    
    df_dx2 = (200 * x[1]) - (200*x[1]**2)
    df_dx1 = (-400 * x[0] * x[1]) + (400 * x[0]**3) - 2 + (2 * x[0])
    return np.array([df_dx1, df_dx2])

def f_doubleprime(x):
    dfx1_dx1 = -400 * x[1] + 1200 * x[0]**2 + 2
    dfx1_dx2 = -400 * x[0]
    dfx2_dx1 = -400 * x[0] 
    dfx2_dx2 = 200

    return np.array([[dfx1_dx1, dfx1_dx2],
                    [dfx2_dx1, dfx2_dx2]])

def dk_cal(xk):

    return -1 * np.linalg.inv(f_doubleprime(xk)) @ fprime(xk)

def left_right(xk, alphak, dk, c):
    left_side = f(xk + alphak * dk)
    right_side = f(xk) + c * alphak * fprime(xk).T @ dk

    print(f'left: {left_side}, right: {right_side}, left > right: {left_side > right_side}')

    return left_side > right_side    

# STILL NEEDS TO TEST THIS**************************************
def newtons_method_line_search(xk):
    
    # set
    k = 0
    eps = m.pow(10, -4)
    dk = dk_cal(xk)

    d = {}
    
    while np.linalg.norm(fprime(xk)) > eps:
        # choose alpha, row, and c
        row = 0.6
        c = 0.22
        alphak = 1
        n = 1
        while left_right(xk, alphak, dk, c):
            print(f'alphak (second while): {alphak} n: {n} dk: {dk}\nfprime@dk: {fprime(x)@dk} fprime.T@dk {fprime(x).T@dk}\n')
            alphak = row * alphak
            n += 1
        print('xk: ', xk, 'k: ', k, 'alphak (first while): ', alphak)
        xk = xk + alphak * dk
        dk = dk_cal(xk)
        k += 1
        print(f'after recalculation xk: {xk} k: {k} alphak (first while): {alphak}\ndk: {dk} fprime@dk: {fprime(x)@dk} fprime.T@dk{fprime(x).T@dk}\n')

        d[tuple(xk)] = [k, alphak, xk]

        if k == 2:
            raise Exception
        
    return d

print(f"f(x1, x2): {f(x)}")
print(f"f'(x1, x2): {fprime(x)}")
print(f"f''(x1, x2): {f_doubleprime(x)}")
print(newtons_method_line_search(x))

'''
first each starting point, print out the step length ak and point xk for every step k.
Newton's Method should converge very fast.
'''

# QUESTION 3
print("\n------------QUESTION 3-----------")
'''
This is written in my notebook
'''

# QUESTION 4
print("\n------------QUESTION 4-----------")

# demand
demand = {'d1': 100, 'd2': 65, 'd3': 95}

# CONSTRAINTS
# generator production upper/lower bounds
p_min = np.array([20, 20, 10])
p_max = np.array([200, 150, 150])

# flow limits
fij_min = np.array([-100, -110, -50, -80, -60, -40])
fij_max = np.array([100, 110, 50, 80, 60, 40])

# branch flow
branch_flow = np.array([11.6, 5.9, 13.7, 9.8, 5.6, 10.5])

# unit generation costs
c = np.array([16, 20, 8])

# PART A
print("---------------------PART A---------------------")
'''
This is written in my notebook.
'''

# PART B
print("---------------------PART B---------------------")
f12 = cp.Variable(1)
f23 = cp.Variable(1)
f34 = cp.Variable(1)
f45 = cp.Variable(1)
f56 = cp.Variable(1)
f61 = cp.Variable(1)
#fij = cp.Variable(6)
p = cp.Variable(3)

expr = cp.sum(cp.multiply(c, p))

obj = cp.Minimize(expr)
constraints =  [p >= p_min, p <= p_max,
                #fij > fij_min, fij <= fig_max,
                f12 >= fij_min[0], f12 <= fij_max[0],
                f23 >= fij_min[1], f23 <= fij_max[1],
                f34 >= fij_min[2], f34 <= fij_max[2],
                f45 >= fij_min[3], f45 <= fij_max[3],
                f56 >= fij_min[4], f56 <= fij_max[4],
                f61 >= fij_min[5], f61 <= fij_max[5],]

#electric = cp.Problem(obj, constraints)
#electric.solve()

# USE THE FINAL VALUES OF FLOW FOR EACH BRANCH HERE
# theta_difference =  flow_limit / branch_flow

# PART C
print("---------------------PART C---------------------")