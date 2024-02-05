#!/usr/bin/python3
""" Module for `lookup()` """


def lookup(obj):
    """
    Function definition for `lookup()`
    Returns: a list of available methods and attributes of an object
    """
    return dir(obj)
