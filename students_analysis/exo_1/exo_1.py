# Most common way
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Complicated way but for getting ued to Python 
def is_number_1(x) :
    # Check if x is a number (int or float) - True
    if isinstance(x, (int, float)) :
        x = float(x)
    
    # Check if x is a string number - True
    if not isinstance(x, str) :
        try : 
            float(x)
        except ValueError :
            return False
    else :
        x = x.replace('"', '')
        try : 
            float(x)
        except ValueError :
            return False

    # Check if x is None - False
    if x == '' :
        return False
    
    # Check if x is a negative string number - True
    if isinstance(x, str) and (x[0] == '-') :
        x = x.replace('"', "")

    # Check if x is a decimal number - True
    dot_count = 0
    for char in str(x) :
        if char == '.' :
            dot_count += 1
            if dot_count > 1 :
                return False 
        elif not char.isdigit() : 
            return False
    
    return True


# Better way
def is_number_2(x) :
    if isinstance(x, str) :
        x = x.replace(' ', '')
        try :
            x = float(x)
        except ValueError : 
            return False
    return x == x + 0


# Shorter and cleaner form of the is_number_1
def is_number_3(x):
    if isinstance(x, bool) :
        return False
    if isinstance(x, (int, float)): 
        return True
    if not isinstance(x, str): 
        return False
    s = x.strip().lstrip('-')
    return s.replace('.', '', 1).replace('"', '').isdigit()


# Another way : using logging

# *** Using these lines to import functions from another folder (pay attention to the number of "parent")
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from log_analysis.logging_config import get_logger

logger = get_logger(__name__)

def is_number_4(x):
    try: 
        return float(x)
    except ValueError as e: 
        logger.exception(f'{e}') 
        # logger.error only displays the error message, while logger.exception shows where the error occurred. 
        raise ValueError('This is not a number.')