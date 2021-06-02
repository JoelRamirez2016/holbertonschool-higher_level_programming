#!/usr/bin/python3
"""This module define the function read_file"""


def read_file(filename=""):
    """Print text in file"""
    with open(filename) as f:
        print(f.read(), end="")
