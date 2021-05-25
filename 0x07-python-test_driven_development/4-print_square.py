#!/usr/bin/python3
"""This module define the function print_square"""


def print_square(size):
    """print a square using #
    Args:
        size (int): len of the square
    Raises:
        TypeError: if size is no a int or if is a float < 0
        ValueError: if size is a int < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
