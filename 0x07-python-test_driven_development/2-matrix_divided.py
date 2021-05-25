#!/usr/bin/python3
"""This module define the function matrix_divided"""


def matrix_divided(matrix, div):
    """Return matrix with all elements of a matrix divided by
    div with 2 precision

    Args:
        matrix: list of lists of integers or floats
        div (int, float): dividend of all matrix elements
    Raises:
        TypeError: if matrix has a not int or float or div is not int or float
        ZeroDivisionError: if div = 0
    """
    if not(isinstance(matrix, list) and matrix != [] and
           all(isinstance(row, list) and row != [] for row in matrix) and
           all(isinstance(c, (float, int)) for r in matrix for c in r)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return list(map(lambda r: [round(c / div, 2) for c in r], matrix))
