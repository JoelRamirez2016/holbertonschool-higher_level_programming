#!/usr/bin/python3
"""This module define the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square inherit of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square
        Args:
            size (int): width and height fo square
            x (int): x position of the rectangle
            y (int): y position of the rectangle
            id: identifier id the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get size(width or height) of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Set size(width or height) of the square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update square attributes
        Args:
            *args
                1 arg: modify id
                2 arg: modify size (width and height)
                3 arg: modify x
                4 arg: modify y
            **kwargs
                attributes to be updated
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
