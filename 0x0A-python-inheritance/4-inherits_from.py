#!/usr/bin/python3
"""This module define the function def inherits_from"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    return issubclass(type(obj), a_class) and not type(obj) == a_class
