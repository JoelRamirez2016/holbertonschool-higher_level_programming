#!/usr/bin/python3
"""This module define the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to save
        filename (str): file name
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
