#!/usr/bin/python3
"""
Module for deserializing JSON strings to object
"""
import json


def from_json_string(my_str):
    """
    Deserializes JSON string to python object
    Args:
        my_str: JSON string
    Returns: the python object
    """
    return json.loads(my_str)
