#!/usr/bin/python3
"""Module for inheritance from function"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
     (directly or indirectly) from the specified class
    Args:
        obj (object): object to be checked
        a_class (class): class to be checked againts

    Returns: True if the object is an instance of a inherited class,
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
