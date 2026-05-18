import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from students_analysis.exo_1.exo_1 import is_number

# solve first-degree equation
def sol_1_eq(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else: return "No solution"
    
    else:    
        x = - b / a
        return x

# solve linear system of equations 
def sol_s_eq(a1, b1, c1, a2, b2, c2):
    # number verification 
    if not is_number(a1) or not is_number(b1) or not is_number(c1) or not is_number(a2) or not is_number(b2) or not is_number(c2):
        return "Inappropriate input(s)"
    
    # Cramer's rules
    D  = float(a1) * float(b2) - float(a2) * float(b1)
    Dx = float(c1) * float(b2) - float(c2) * float(b1)
    Dy = float(a1) * float(c2) - float(a2) * float(c1)
    if D == 0:
        if Dx == 0 and Dy == 0:
            return "Infinite solutions"
        else:
            return "Can't solve"
    else:
        x = Dx / D
        y = Dy / D
        return f'x = {x}, y = {y}'

# solve second-degree equation  
def sol_2_eq(a, b, c):
    # number verification 
    if not is_number(a) or not is_number(b) or not is_number(c):
        return "Inappropriate input(s)"

    # resolution
    if a == 0:
        x = - float(c) / float(b)
        return f'Unique solution : x = {x}'
    else:
        delta = float(b)**2 - 4*float(a)*float(c)

        if delta < 0:
            return "Complex solutions"
        elif delta == 0:
            x = -float(b) / (2*float(a))
            return f'Double solutions : x = {x}'
        else:
            x1 = (-float(b) + delta**0.5) / (2*float(a))
            x2 = (-float(b) - delta**0.5) / (2*float(a))
            return f'2 different solutions : x1 = {x1}, x2 = {x2}'