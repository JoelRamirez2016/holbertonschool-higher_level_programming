#!/usr/bin/python3
"""This module define the lookup function"""


def lookup(obj):
    """Get the list of available attributes and methods of an object
    Args:
        obj (object): object to be checked
    Return:
        list of arguments
    """
    return dir(obj)
