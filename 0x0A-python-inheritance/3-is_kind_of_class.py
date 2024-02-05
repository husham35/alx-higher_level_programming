#!/usr/bin/python3
"""Module for `is_kind_of_class`"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    Args:
        obj (object): Object to check
        a_class (class): Class to check against

    Returns: True if object is an instance of inherited class, False otherwise
    """
    return isinstance(obj, a_class)
