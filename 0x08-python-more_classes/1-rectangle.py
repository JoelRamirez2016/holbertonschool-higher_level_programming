#!/usr/bin/python3
"""This file create the Rectangle class"""


class Rectangle:
    """Define the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Inicializate of a Rectangle

        Args:
            width (int): width of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/seter of width attr"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self, height):
        """Get/seter of height attr"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
