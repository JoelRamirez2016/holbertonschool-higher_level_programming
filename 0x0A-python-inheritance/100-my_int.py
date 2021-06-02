#!/usr/bin/python3
"""This module define the class MyInt"""


class MyInt(int):
    """This class represents an integer inheriting from int"""

    def __eq__(self, other):
        """Return the eq comparison of Myint != int"""
        return self.real != other

    def __ne__(self, other):
        """Return the eq comparison of Myint == int"""
        return self.real == other
