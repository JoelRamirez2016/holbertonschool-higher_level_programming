#!/usr/bin/python3
"""This module define the class BaseGeometry"""


class BaseGeometry:
    """This function has not been implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function check for a int parameter
        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError if value not is an integer"
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
