#!/usr/bin/python3
"""
Module for writing a a file
"""


def write_file(filename="", text=""):
    """
    Writes text to a file in utf-8 encoding
    Args:
        filename: the filename to write to
        text: content to write to file
    Returns: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
