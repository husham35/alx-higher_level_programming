#!/usr/bin/python3
"""Module for `is_same_class`"""


def is_same_class(obj, a_class):
    """
    Check if `obj` is an instance of `a_class`
    Args:
        obj (object): object to check
        a_class (object): any class object to check
    Returns:
        `True` if `obj` is exactly an instance of the
         specified class else `False`
    """
    return type(obj) is a_class
