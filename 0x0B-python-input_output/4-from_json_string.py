#!/usr/bin/python3
"""This module define the from_json_string function"""
import json


def from_json_string(my_str):
    """Create an object (Python data structure) represented by a JSON string
    Args:
        my_str (str): JSON string of the object
    Return
        object represented by my_str
    """
    return json.loads(my_str)
