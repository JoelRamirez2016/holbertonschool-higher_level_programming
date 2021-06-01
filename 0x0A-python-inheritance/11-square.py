#!/usr/bin/python3
"""This module define a Square class inherit from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this class is a representation of a Square"""
    def __init__(self, size):
        """Inicialize a new Square
        Args:
            size (int): size of the square
        """
        super(Square, self).__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
