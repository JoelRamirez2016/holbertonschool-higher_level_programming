#!/usr/bin/python3
"""This module define the Student Class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a student
        Args:
             first_name (str)
             last_name (str)
             age (str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the dictionary description of some attributes the student
        Args:
           attrs: attributes to get
           obj: object with __dict__ attr
        Returns:
           dictionary description of the student
        """
        if type(attrs) == list and all(type(e) == str for e in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
