
# IMPORTS


# QUESTION 1
print("------------QUESTION 1-----------")
'''
ANSWER: No solution. If x and y must both be <= 0, then x + y = 1 will never be met, therefore the feasible set is empty.
'''

# QUESTION 2
print("\n------------QUESTION 2-----------")

# PART A
print("\n***PART A***")
'''
ANSWER: There are infinitly many global minimum solutions. See graph.
'''

# PART B
print("\n***PART B***")
'''
ANSWER: No, per the solution above you can see that all solutions are at y = 0 for infinitly many x in R.
'''

# PART C
print("\n***PART C***")
'''
A twice differentiable univarate function f: R > R is convex if f''(x) >= 0 for all X in R
ANSWER: No this function is not convex as the f'' is not >= 0 for all x in R. In fact, it continues to grow towards -inf
'''

# QUESTION 3
print("\n------------QUESTION 3-----------")
'''
ANSWER: There is no optimal solution. As x approaches +inf the objective function will continue to get infinitly small. You will always be able to find a bigger x that will make 1/x smaller.
'''

# QUESTION 4
print("\n------------QUESTION 4-----------")

# PART A
print("\n***PART A***")
'''
ANSWER: Regarding the full optimization problem, when plotting x + f(x) you can see no clear definition of convexity. You can't do any derivated tests because it is discontinuous and therefore not differentiable. You can't check a line segment from 1 point to another 1 is above the function because of the infinity portion and discontinuity. Convexity is not preserved when adding two convex functions because f(x) is not convex. The one test you can do is the function test, which works except for the fact that a function can't equal infinity, but if we assume it can then it is convex
'''

# PART B
print("\n***PART B***")
'''
ANSWER: There are no optimal solutions. The inequality -1 < x < 1 will yield the lowest values, but you can find infinitly many x's that are close to -1. This means that you will always be able to find a smaller x that is infinitly close to 1. The result is that there is no optimal solution.
'''

# QUESTION 5
print("\n------------QUESTION 5-----------")

# PART A
print("\n***PART A***")
'''
False, take f(x) = x^2 and g(x) = x^3 >= 0. For this case the optimal value = 0. For g(x) >= 1, the new optimal value = 1. An optimal value of 1 is > 0 not <=.
'''

# PART B
print("\n***PART B***")
'''
True, f(x) is nonconvex, but f(x)^4 is convex. Therefore if f(x*) = 0, then f(x*)^4 = 0 and is therefore a global optimal solution.
'''

# PART C
print("\n***PART C***")
'''
True. In the lecture we had vp = min{f(x)}, vd = max{min{}} on lam >= 0 , and vd <= vp. In this example, we have vp = max {f(x)} and min{max{}} on lam >= 0. We can also see that in the lecture we had g(x) <= b_i and here we have g(x) >= b_i. If v_p is the solution for (P) and vd the solution for (D), then the Lagrangian = max(v_p + summation of lambda(g(x)-b). The summation will be >= 0 because g(x) >= b_i and lambda >= 0. v_p + a value that is >= 0 means that vd >= vp
'''