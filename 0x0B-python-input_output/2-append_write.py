#!/usr/bin/python3
"""This module defines the add write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename (str): file name
        text (str): text to write
    Returns:
        the number of characters added
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
