
#IMPORTS
import numpy as np

# QUESTION 2
# PART A
dimension = 3

# PART B


# PART C


# PART D


# PART E


# PART F


# PART G



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


# PART B


# PART C


# QUESTION 4
def fnc_convex(f, x:np.array, y:np.array, lam:float):
    """if return array is in X then function is convex

    Args:
        f (function_): function required to be passed
        x (np.array): vector in X
        y (np.array): vector in X
        lam (float): lambda value

    Returns:
        _type_: _description_
    """
    return f((lam * x) + ((1 - lam) * y)) <= (lam * f(x)) + ((1 - lam) * f(y))

# PART A


# PART B


# PART C