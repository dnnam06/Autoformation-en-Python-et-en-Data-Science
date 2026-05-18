# build a factorial calculor with the Math library 
import math 

def factorial_calculator(n):
    if n == 0:
        return 1
    return math.factorial(n)

# usual way to solve the problem
def factorial_calculator_1(n): 
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for number in range(1, n+1):
            result = result * number
        return result

print(factorial_calculator_1(5))

# solve the problem with recursion
def factorial_calculator_2(n): 
    # Condition to not repeat infinitely
    if n == 0 or n == 1:
        return 1
    # Recursion
    else:
        return n * factorial_calculator_2(n - 1)