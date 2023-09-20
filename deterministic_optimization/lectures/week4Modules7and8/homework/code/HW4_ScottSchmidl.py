# IMPORTS
import math as m
import scipy.optimize as so

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


stop = True
x = -1
n = 0

while stop:

    xx = f(x)
    x_x = f_prime(x)
    x_xx = f_doubleprime(x)
    next_x = x - (x_x / x_xx)
    
    print(f'step {n}:\nx: {x}\nf(x): {xx}\nf\'(x): {x_x}\nf\'\'(x): {x_xx}\nfinal_x: {next_x}')

    if abs(x_x) < 10**-5:
        stop = False

    x = next_x 
    n += 1

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

print('ANSWER: IN .DOCX')



# NONCONVEX OPTIMIZATION
print("\n-----------NONCONVEX OPTIMIZATION-----------")

# QUESTION 1
print("\n------------QUESTION 1-----------")
'''
x1 >= -5
x2 <= 5

box = [[-5, 5],
       [5, -5]]

'''


def f_part2q1(x):
    return (1 - x1 + (x1 * x2))**2 + (2 - x1 + ((x1**2) * x2))**2 + (3 - x1 + ((x1**3) * x2))**2

# type(mini) = dictionary

x = []
d = {}
for x1 in range(-5, 6):
    for x2 in range(5, -6, -1):
        x = [x1, x2]
        mini = so.minimize(fun=f_part2q1, x0=x, method='Nelder-Mead')
        d[x1,x2] = mini['fun']

print(d[(0,0)])


# QUESTION 2
print("\n------------QUESTION 2-----------")

'''

'''

