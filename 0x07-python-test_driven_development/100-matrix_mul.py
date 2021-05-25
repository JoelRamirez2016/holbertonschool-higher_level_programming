#!/usr/bin/python3
"""This module define the function matrix_mul"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    Raises:
        TypeError: if either m_a or m_b is not a list of lists of ints/floats
        if m_a or m_b is empty
        if m_a or m_b has different-sized rows
        ValueError: If m_a and m_b cannot be multiplied
    Return:
        new matrix of m_a * m_b
    """

    if not isinstance(m_a , list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b , list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(r_a , list) for r_a in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r_b , list) for r_b in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or all(r_a == [] for r_a in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or all(r_b == [] for r_b in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(n_a , (float, int)) for r_a in m_a for n_a in r_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n_b , (float, int)) for r_b in m_b for n_b in r_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(r_a) == len(m_a[0]) for r_a in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(r_b) == len(m_b[0]) for r_b in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
       row = []
       for j in range(len(m_b[0])):
           row.append(sum([m_a[i][k] * m_b[k][j] for k in range(len(m_b))]))
       result.append(row)
    return result
