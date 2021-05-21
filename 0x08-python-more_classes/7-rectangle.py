#!/use/bin/python3
"""This file create the Rectangle class"""


class Rectangle:
    """Define the Rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        number_of_instances (int): number of Rectangle instances created
        print_symbol (str): symbol to be printed in the Rectangle 
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializate of a Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Create a string repesentation of the rectangle using #
        """
        string = ""

        for h in range(self.__height):
            if self.__width == 0:
                break
            string += str(self.print_symbol) * self.__width

            if h + 1 != self.__height:
                string += "\n"

        return string

    def __repr__(self):
        """Create a string representation of the Rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the instance Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
