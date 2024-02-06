#!/usr/bin/python3
"""
Module for creating an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Function to load an object from a JSON file
    Args:
        filename: the file to read from
    Returns: the loaded object
    """
    with open(filename, mode="r", encoding="utf-8") as jf:
        return json.load(jf)
