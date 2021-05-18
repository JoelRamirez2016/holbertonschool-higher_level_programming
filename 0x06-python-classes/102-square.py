#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square: This class define a Square

    Attributes:
        size (int): area of the square, must be an integer and >=0

    """
    def __init__(self, size=0):
        """ __init__ method (self, size).

        Args:
            size (:`int`, optional): integer to define size of the
                squeare
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: getter of the squeare size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter of the square size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """int: area of the squeare based in size attr"""
        return self.__size * self.__size

    def __lt__(self, other):
        """Define comparison < between two Squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define comparison <= between two Squares"""
        return self.area() <= other.area()  

    def __eq__(self, other):
        """Define comparison == between two Squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define comparison != between two Squares"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define comparison > between two Squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define comparison >= between two Squares"""
        return self.area() >= other.area()

