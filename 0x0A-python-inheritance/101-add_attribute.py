#!/usr/bin/python3
"""This module define the function add_attribute"""


def add_attribute(obj, attr, val):
    """Add a new atribute in object
    Args:
        obj (object): objecto to add the new atribute
        attr (str): name of the atribute
        val (object): value of the atribute
    Raises:
        TypeError if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
