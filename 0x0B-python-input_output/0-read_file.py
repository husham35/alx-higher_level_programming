#!/usr/bin/python3
"""Module for reading a text file"""


def read_file(filename=""):
    """
    Reads a text from a file and prints it to stdout
    Args:
        filename (str): the name of the file to read
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
