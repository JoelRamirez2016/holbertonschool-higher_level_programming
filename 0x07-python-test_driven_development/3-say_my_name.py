#!/usr/bin/python3
"""This module define the function say_my_name"""


def say_my_name(first_name, last_name=""):
    """This function prints My name is <first name> <last name>
    Args:
        first_name (str)
        last_name (optional) (str)
    Raises:
        TypeError if first_name or last_name are not str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + (" " + last_name if last_name else ""))
