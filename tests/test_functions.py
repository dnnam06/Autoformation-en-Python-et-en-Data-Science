from functions_pytest import sol_1_eq, sol_2_eq, sol_s_eq
import pytest
# to run : pytest -v

# Coding to test the function solving first-degree equation
def test_sol_1_eq() :
    assert sol_1_eq(2, 4) == -2.0
    assert sol_1_eq(0, 4) == "No solution"
    assert sol_1_eq(0, 0) == "Infinite solutions"

# Coding to test the function solving second-degree equation
def test_sol_2_eq() :
    assert sol_2_eq(2, 2, 2) == "Complex solutions"
    assert sol_2_eq(1, 2, 1) == "Double solutions : x = -1.0"
    assert sol_2_eq('e', 2, 2) == "Inappropriate input(s)"
    assert sol_2_eq('2 ', -10, 12) == '2 different solutions : x1 = 3.0, x2 = 2.0'
    assert sol_2_eq(0, 2, 2) == "Unique solution : x = -1.0"

# Coding to test the function solving linear system of equations
def test_sol_s_eq() :
    assert sol_s_eq(2, 2, 2, 2, 2, 1) == "Can't solve"
    assert sol_s_eq(2, 2, 2, 2, 2, 2) == "Infinite solutions"
    assert sol_s_eq('e', 2, 2, 2, 2, 2) == "Inappropriate input(s)"
    assert sol_s_eq('2 ', 1, 2, 2, 2, 2) == 'x = 1.0, y = 0.0'