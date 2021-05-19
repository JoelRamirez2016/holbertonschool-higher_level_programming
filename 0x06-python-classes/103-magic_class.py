#!/usr/bin/python3
"""Definition of the MagicClass"""

import math


class MagicClass:
    """Representation of a circle
    Args:
        radius (float)(int): radius of the circle
    """

    def __init__(self, radius=0):
        """ init function of MagicClass
        Args:
            radius (float)(int): radius of the circle
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return: area of the cicle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return: area of the circumference"""
        return 2 * math.pi * self.__radius
