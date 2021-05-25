#!/usr/bin/python3
"""This module define add_integer function"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    Args:
        a (int, float): first number
        b (int, float): second number. default value 98
    Raises:
        TypeError: if a or b not are (int, float)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
