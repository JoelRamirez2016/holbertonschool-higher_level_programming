#!/usr/bin/python3
"""Define the function lazy_matrix_mul"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix using numpy
    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    Return:
        matrix result representing m_a * m_b
    """
    return np.matmul(m_a, m_b)
