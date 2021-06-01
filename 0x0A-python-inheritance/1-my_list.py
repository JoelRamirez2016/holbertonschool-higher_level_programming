#!/usr/bin/python3
"""This module define the class MyList"""


class MyList(list):
    """This class define a list inherit of list
    """
    def print_sorted(self):
        """Print the list in ascending sort"""
        print(sorted(self))
