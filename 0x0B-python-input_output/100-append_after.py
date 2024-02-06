#!/usr/bin/python3
"""Searches and appends a file with new string"""


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file, after each line containing
        a specific string.
    Args:
        filename: name of file
        search_string: string to search for
        new_string: string to be appended
    """
    with open(filename, mode="r", encoding="utf-8") as s:
        lines = s.readlines()

    new_lines = []
    for line in lines:
        if search_string in line:
            new_lines.extend((line, new_string))
        else:
            new_lines.append(line)

    with open(filename, mode="w", encoding="utf-8") as s:
        s.writelines(new_lines)
