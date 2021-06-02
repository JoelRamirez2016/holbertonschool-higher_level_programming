#!/usr/bin/python3
"""This module define the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each
    line containing a specific string
    Args:
        filename (str): file name to be checked
        search_string (str): text to comparete in each line
        new_string (str): new line to add
    """
    with open(filename, "r") as f:
        contents = f.readlines()

    contents = list(
                   map(
                       lambda l: l + new_string if search_string in l else l,
                       contents
                   )
               )

    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
