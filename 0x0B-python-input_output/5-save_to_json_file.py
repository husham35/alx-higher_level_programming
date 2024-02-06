#!/usr/bin/python3
"""
Module for saving an object to a json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a json file
    Args:
        my_obj: python object to be saved in JSON format
        filename: the file to contain the JSON contents
    Returns: nothing
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)