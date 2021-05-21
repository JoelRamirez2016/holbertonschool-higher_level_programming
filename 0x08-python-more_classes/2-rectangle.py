#!/usr/bin/python3
"""This file create the Rectangle class"""


class Rectangle:
    """Define the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Inicializate of a Rectangle

        Args:
            width (int): width of the rectangle
        """
        self.width = width
        self.height = height

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
    def height(self):
        """Get/seter of height attr"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Get the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Get the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
