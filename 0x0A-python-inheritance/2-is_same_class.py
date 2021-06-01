#!/usr/bin/python3
"""This module define the function is_same_class"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class
    """
    return type(obj) == a_class
