#!/usr/bin/python3
"""This module define the Base class"""


class Base:
    """Represent a Geometry Base
    Args:
        nb_objects (int): number of base class instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
