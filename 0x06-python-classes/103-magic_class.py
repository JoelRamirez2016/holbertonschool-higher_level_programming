#!/usr/bin/python3
""" descrip """

import math


class MagicClass:
    """ descrip """

    def __init__(self, radius=0):
        """ descrip """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ descrip """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ descrip """
        return 2 * math.pi * self.__radius
