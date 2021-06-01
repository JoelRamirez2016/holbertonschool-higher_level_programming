#!/usr/bin/python3
"""This module define the Rectangle class inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a representation of a rectangle
    """
    def __init__(self, width, height):
        """Intialize a new Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height
