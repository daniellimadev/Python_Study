"""This is an example module
This module contains functions and function documentation examples.
You already know a lot about the sum function.
"""
variable_1 = 1

# def sum(x, y):


def sum(x: int | float, y: int | float) -> int | float:
    """Sum x and y
    This module contains functions and function documentation examples.
    You already know a lot about the sum function.
    :param x: Number 1
    :type x: int or float
    :param y: Number 2
    :type y: int or float
    :return: The sum of x and y
    :rtype: int or float
    """
    return x + y


def multiply(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    """Multiplies x, y and/or z
    Multiplies x and y. If z is sent, multiply x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z


variable_2 = 2
variable_3 = 3
variable_4 = 4