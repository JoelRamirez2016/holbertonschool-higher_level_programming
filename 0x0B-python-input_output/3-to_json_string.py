#!/usr/bin/python3
"""This module define the to_json_string function"""
import json


def to_json_string(my_obj):
    """Create a JSON representation of an object
    Args:
        my_obj (object)
    Return
        (str) JSON representation of the object
    """
    return json.dumps(my_obj)
