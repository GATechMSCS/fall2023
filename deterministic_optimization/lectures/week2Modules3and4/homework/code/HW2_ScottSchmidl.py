
#IMPORTS
import numpy as np

# QUESTION 1
'''This question is directly in the homework .docx file'''

# QUESTION 2
x = np.array([1, 2, 3])#.reshape(3,1)
y = np.array([3,2,1])#.reshape(3,1)
A = np.array([[1, -2, 3],
             [-2, 3, -1],
             [3, -1, 2]])
print(x, '\n', y, '\n', A )

# PART A
dimension = 3
print(dimension)

# PART B
print(2*x - y)

# PART C
print(np.inner(x.T, y))

# PART D
''' decimal version of the sqrt of 8'''
l2_norm = np.linalg.norm(x-y, ord=2) 
print(l2_norm)

# square value
assert round(np.square(l2_norm)) == 8
print(f'is the square of norm = 8? {round(np.square(l2_norm), 2) == 8}')

# PART E
l1_norm = np.linalg.norm(x-y, ord=1) 
print(round(l1_norm))

# PART F
inf_norm = np.linalg.norm(x-y, ord=np.inf)
print(round(inf_norm))

# PART G
''' The @ operator is shorthand for np.matmul on ndarrays.'''
m = x.T @ A @ y
print(m)

# QUESTION 3
def set_convex(x:np.array, y:np.array, lam:float):
    """if return array is in X then set is convex

    Args:
        x (np.array): vector in X
        y (np.array): vector in X
        lam (float): lambda value

    Returns:
        np.array: point to check if in X
    """
    return (lam * x) + (1 - lam) * y

# PART A
x1 = np.array([-2, 0])
x2 = np.array([2, 0])
lam = 0.5
print(set_convex(x1, x2, lam))

# PART B
x1 = np.array([-1.414])
x2 = np.array([1.414])
lam = 0.5
print(set_convex(x1, x2, lam))

# PART C
'''The graph of x_{1} >= 1 is unbounded making the Math hard, but you can see from the graph that this is convex.'''

# QUESTION 4
def fnc_convex(f, x:np.array, y:np.array, lam:float):
    """if return array is in X then function is convex

    Args:
        f (function_): function required to be passed
        x (np.array): vector in X
        y (np.array): vector in X
        lam (float): lambda value

    Returns:
        boolean: whether the inequality is true or false
    """
    return f((lam * x) + ((1 - lam) * y)) <= (lam * f(x)) + ((1 - lam) * f(y))

# PART A
'''Program is convex'''

# PART B
'''Program is not convex'''

# PART C
'''Program is not convex'''

# QUESTION 5

# PART A
'''This question is directly in the homework .docx file'''

# PART B
'''This question is directly in the homework .docx file'''

# PART C
'''This question is directly in the homework .docx file'''