#!/usr/bin/python3
"""This module define the function write_file"""


def write_file(filename="", text=""):
    """Write a text to an existing or new file
    Args:
        filename (str): file name
        text (str): text to write
    Return:
        number of characters written
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
