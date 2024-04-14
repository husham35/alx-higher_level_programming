#!/usr/bin/python3
"""
Module for the class MyInt
"""


class MyInt(int):
    """ a rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """instantiating of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
