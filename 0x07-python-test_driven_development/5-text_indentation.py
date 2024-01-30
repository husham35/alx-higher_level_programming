#!/usr/bin/python3
"""Module definition for `text_indentation` function"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of
    these characters: `.`, `?` and `:`
    Args:
        text: (str) text to be printed
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ""
    splitted = []
    delims = ".?:"

    for char in text:
        chars += char
        if char in delims:
            splitted.append(chars.strip())
            chars = ""

    if chars:
        splitted.append("".join(chars).strip())

    for ln in splitted[:-1]:
        print(ln)
        print("")
    print(splitted[-1], end="")
