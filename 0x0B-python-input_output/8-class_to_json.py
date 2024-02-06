#!/usr/bin/python3
"""
Module to convert dictionary description with data structures
"""


def class_to_json(obj):
    """
    Function to convert dictionary description with data structures
    Args:
        obj: an instance of class
    Returns: dictionary description of obj (__dict__)
    """
    return obj.__dict__
