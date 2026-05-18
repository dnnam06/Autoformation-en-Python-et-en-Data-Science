from log_analysis.logging_config import get_logger, setup_logging

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from students_analysis.exo_1.exo_1 import is_number_4

# Get logger for this module
logger = get_logger(__name__)

def calculate(a, b):
    logger.info(f"Calculating: {a} + {b}")
    result = a + b
    logger.debug(f"Result: {result}")
    return result

def divide(a, b):
    logger.info(f"Calculating: {a} / {b}")
    try:
        result = a / b
        logger.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.exception("Cannot divide")
        raise # raise stops the program and propagates the error

if __name__ == "__main__":
    setup_logging()
    
    # Examples:

    # calculate(5, 3)

    # divide(10, 2)

    # divide(10, 0)
    
    try:
        is_number_4('c')
    except Exception as e:
        print(f'{e}')