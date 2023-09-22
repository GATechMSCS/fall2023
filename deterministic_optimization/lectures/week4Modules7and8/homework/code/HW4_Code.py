# IMPORTS
import math as m
import scipy
import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.ticker import LinearLocator

# CONVEX OPTIMIZATION
print("-----------CONVEX OPTIMIZATION-----------")

# QUESTION 1
print("------------QUESTION 1-----------")
'''
1) first-order and second-order derivatives of f(x)
2) a step in the Newton's method, e.g. x^(k+1) = x^k - f'(x^k) / f''(x^k)
3) Carry out the Newton's method from the initial point x0 = -1
4) Write down x^k, f(x^k ), f'(x^k) in each iteration, until you reach a solution with the first-order derivative |f'(x^k)| < 10^-5
'''

def f(x):
    return (m.e**x) - x

def f_prime(x):
    return m.e**x - 1

def f_doubleprime(x):
    return m.e**x

def get_next_x():

    stop = True
    x = -1
    n = 1
    d = {}
    while True:

        xx = f(x)
        x_x = f_prime(x)
        x_xx = f_doubleprime(x)
        next_x = x - (x_x / x_xx)

        if abs(x_x) < 10**-5:
            break

        d[n] = [{'x': x}, {'f(x)': xx}, {'f\'(x)': x_x}, {'f\'\'(x)': x_xx}, {'next_x': next_x}]
        print(f"\nstep {n}\nx: {x}\nf(x): {xx}\nf\'(x): {x_x}\nf\'\'(x): {x_xx}\nnext_x: {next_x}")

        x = next_x 
        n += 1
    return d

get_next_x()

# QUESTION 2
print("\n------------QUESTION 2-----------")
'''
1) First, write down the tangent line of the curve y = f'(x) at a point x^k. Hint: the line passing through the point (x = a, y = b) with slope k has the equation y = k(x - a) + b.
2) Suppose your equation for the tangent line is y = k(x - a) + b. Of course, you need to fill in k, a, b and express them in x^k , f'(x^k), f''(x^k).
3) Then solve the equation k(x - a) + b = 0 and write down the expression of the solution in k, a, b. The solution is the next iteration x^(k+1). If you have
done everything correctly, you should recover the Newton's iterate.
4) The next step of Newton's method starts from x^(k+1), forms the tangent line of the curve y = f'(x) at x'(k+1), and finds the zero of this linear equation,
and continues.
5) Plot y = f'(x) for f(x) = e^x - x. Start from x0 = -1. Draw the tangent line at x0, find the zero, and continue, until you reach x2. You should see the same sequence as you find in the first question, and this should give you a geometric understanding of Newton's method.
'''

print('ANSWER: Plots made in Desmos')

# NONCONVEX OPTIMIZATION
print("\n-----------NONCONVEX OPTIMIZATION-----------")

# QUESTION 1
print("\n------------QUESTION 1-----------")
'''
x1 >= -5
x2 <= 5

box = [[-5, 5],
       [-5, 5]]
'''

def f_part2q1(x):

    x1 = x[0]
    x2 = x[1]
    
    return (1 - x1 + (x1 * x2))**2 + (2 - x1 + ((x1**2) * x2))**2 + (3 - x1 + ((x1**3) * x2))**2

bounds1 = [(-5, 5), (-5, 5)]
mini1 = so.minimize(fun=f_part2q1, x0=[0, 0], method='Nelder-Mead', bounds=bounds1)
print(f"ANSWER:\n{mini1}")

# HELPER FUNCTION FOR PLOTS
def create_grid_func_part2q1():
    delta = 0.2
    x = np.arange(-5.0, 5.0, delta)
    y = np.arange(-5.0, 5.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = (1 - X + (X * Y))**2
    Z2 = (2 - X + ((X**2) * Y))**2
    Z3 = (3 - X + ((X**3) * Y))**2
    Z = Z1 + Z2 + Z3

    return X, Y, Z

# PLOT 2D
def plot_part2q1_2dcontour(X, Y, Z):

    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, levels=range(1, 100))
    ax.clabel(CS, inline=True,  fontsize=10)
    ax.set_title('Contours')

    plt.show()

    return 1

X_q1, Y_q1, Z_q1 = create_grid_func_part2q1()
plot_part2q1_2dcontour(X_q1, Y_q1, Z_q1)

# PLOT 3D
def plot_part2q1_3d(X, Y, Z):

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    ax.set_zlim(-50000, 450000)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

    return 1

plot_part2q1_3d(X_q1, Y_q1, Z_q1)

# QUESTION 2
print("\n------------QUESTION 2-----------")
'''
x1 >= -10
x2 <= 10

box = [[-10, 10],
       [-10, 10]]
'''

def f_part2q2(x):

    x1 = x[0]
    x2 = x[1]
    
    return -0.0001 * (abs(m.sin(x1) * m.sin(x2) * m.e**(abs(100 - (m.sqrt(x1**2 + x2**2) / m.pi)))) + 1)**0.1

bounds2 = [(-10, 10), (-10, 10)]
        
mini21 = so.minimize(fun=f_part2q2, x0=[0, 0], method='Nelder-Mead', bounds=bounds2)
print(f"ANSWER:\n{mini21}")

mini24 = so.minimize(fun=f_part2q2, x0=[9, 9], method='Nelder-Mead', bounds=bounds2)
print(f"ANSWER:\n{mini24}")

mini27 = so.minimize(fun=f_part2q2, x0=[-1, -1], method='Nelder-Mead', bounds=bounds2)
print(f"ANSWER:\n{mini27}")

# HELPER FUNCTION FOR PLOTS
def creat_grid_func_part2q2():
    delta = 0.1
    x = np.arange(-10.0, 10.0, delta)
    y = np.arange(-10.0, 10.0, delta)
    X, Y = np.meshgrid(x, y)

    inside_abs = np.abs(100 - (np.sqrt(np.power(X, 2) + np.power(Y, 2)) / np.pi))
    outside_abs = np.abs(np.multiply(np.sin(X), np.sin(Y), np.exp(inside_abs)))
    tiny_exponent = np.power(outside_abs + 1, 0.1)
    Z = np.multiply(-0.0001, tiny_exponent)

    return X, Y, Z

# PLOT 2D
def plot_part2q2_2dcontour(X, Y, Z):

    fig, ax = plt.subplots(1, 1)
    
    ax.contour(X, Y, Z)
    
    ax.set_title('Contour Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    plt.show()

    return 1

X_q2, Y_q2, Z_q2 = creat_grid_func_part2q2()
plot_part2q2_2dcontour(X_q2, Y_q2, Z_q2)

# PLOT 3D
def plot_part2q2_3d(X, Y, Z):

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues,
                        linewidth=0, antialiased=False)

    fig.colorbar(surf,orientation='vertical',  shrink=.5, aspect=10)

    plt.show()
    
    return 1

plot_part2q2_3d(X_q2, Y_q2, Z_q2)