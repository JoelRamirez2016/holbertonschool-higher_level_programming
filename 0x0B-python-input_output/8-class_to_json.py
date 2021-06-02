#!/usr/bin/python3
"""This module define the class_to_json function"""


def class_to_json(obj):
    """Get the dictionary description with simple data structure
    Args:
        obj: object with __dict__ attr
    Returns:
        dictionary description with simple data structure of the object
    """
    return obj.__dict__
