#!/usr/bin/python3
"""
This module returns the sum of 2 integers
"""


def add_integer(a, b=98):
    """
    Adds and returns the result of 2 integers
    :param a: int|float, first number
    :param b: int|float, second number
    :return: int, sum of the 2 numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
