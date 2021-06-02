#!/usr/bin/python3
"""This module define the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
        filename (str): JSON file name
    """
    obj = None

    with open(filename) as f:
        obj = json.loads(f.read())
    return obj
