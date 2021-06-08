#!/usr/bin/python3
"""This module define the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representation of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x position of the rectangle
            y (int): y position of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width attribute"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height attribute"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x attribute"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y attribute"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the rectangle area
        Return:
            area value of the Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """Print the Rectangle instance with the character #"""
        row = " " * self.x + "#" * self.__width + "\n"
        print("\n" * self.y + row * self.__height, end="")

    def __str__(self):
        """Return str representation of a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
               self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle attributes
        Args:
            *args
                1 arg: modify id
                2 arg: modify width
                3 arg: modify height
                4 arg: modify x
                5 arg: modify y
            **kwargs
                attributes to be updated
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'height': self.height, 'width': self.width,
                'x': self.x, 'y': self.y}
