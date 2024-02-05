#!/usr/bin/python3
"""
This module contains `MyList` class definition
"""


class MyList(list):
    """ MyList class that inherits from `list` class"""
    def print_sorted(self):
        """ Prints the sorted list"""
        print(sorted(self))