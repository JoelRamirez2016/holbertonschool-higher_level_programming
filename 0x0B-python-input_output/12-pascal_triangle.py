#!/usr/bin/python3
"""This module define the pascal_triangle function"""


def pascal_triangle(n):
    """Get a list of lists of ints representing the Pascal’s triangle of n
    Args:
        n (Always int): triangle height
    Return:
        list of lists of ints
    """
    pascal = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)

    return pascal
