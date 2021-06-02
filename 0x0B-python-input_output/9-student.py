#!/usr/bin/python3
"""This module define the Student Class"""


class Student:
    """Representation of a student"""
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

    def to_json(self):
        """Get the dictionary description iof the student instance
        Args:
           obj: object with __dict__ attr
        Returns:
           dictionary description of the student
        """
        return self.__dict__
