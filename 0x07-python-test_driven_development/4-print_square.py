#!/usr/bin/python3
"""Module for the definition of `print_square` function"""


def print_square(size):
    """
    Prints square with `#` character
    Args:
        size: (int) size of the square to print
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is not a positive number
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
    print("")
