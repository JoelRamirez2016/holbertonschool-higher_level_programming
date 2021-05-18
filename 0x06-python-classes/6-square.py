#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square: This class define a Square

    Attributes:
        size (int): area of the square, must be an integer and >=0

    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method (self, size).

        Args:
            size (:`int`, optional): integer to define size of the
                squeare
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (type(position) == tuple and
                len(position) == 2 and
                type(position[0]) == int and
                type(position[1]) == int and
                all(v >= 0 for v in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def position(self):
        """int: getter of the squeare position"""
        return self.__position

    @property
    def size(self):
        """int: getter of the squeare size"""
        return self.__size

    @position.setter
    def position(self, position):
        if not (type(position) == tuple and
                len(position) == 2 and
                type(position[0]) == int and
                type(position[1]) == int and
                all(v >= 0 for v in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """print the square with the size attr"""
        if self.__size == 0:
            print("")
            return
        square = "".join(["\n" for c in range(self.__position[1])])
        for i in range(0, self.__size):
            square += "".join([" " for c in range(0, self.__position[0])])
            for j in range(0, self.__size):
                square += "#"
            square += "\n"
        print(square, end="")
