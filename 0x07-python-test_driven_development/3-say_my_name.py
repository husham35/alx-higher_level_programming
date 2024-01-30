#!/usr/bin/python3
"""Module for the definition of `say_my_name` function"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's full name
    Args:
        first_name: (str) first name
        last_name: (str) last name

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
