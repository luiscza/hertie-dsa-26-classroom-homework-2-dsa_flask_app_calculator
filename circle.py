# create helper functions for calculations
import math


def make_circle(value1: float, operation: str) -> float:
    """
    Perform a mathematical operation on one value.

    Parameters:
        value1 (float): The first value.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'divide', or 'multiply'.

    Returns:
        float: The result of the operation.
    """
    if operation == 'perimeter':
        result = 2 * value1 * math.pi
    elif operation == 'area':
        result = math.pi * (value1 ** 2 )

    return result


def convert_to_float(value: str) -> float:
    """
    Convert string to floating point number.

    Parameters:
        value (str): The value to convert.

    Returns:
        float: The converted float value of input value.

    Raises:
        ValueError: If value cannot be converted to a float.
    """

    float_value = float(value)

    return float_value