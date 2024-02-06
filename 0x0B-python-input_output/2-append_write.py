#!/usr/bin/python3
"""
Module for appending a string at the end of an existing
file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of an existing file
    Args:
        filename: the name of the file to append to
        text: the text to append to the file
    Returns: the number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
