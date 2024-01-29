#!/usr/bin/python3
"""Module contains a class Rectangle"""


class Rectangle:
    """Rectangle class definition"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle class
        :param width: (int) width of the rectangle
        :param height: (int) height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height of the"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be a >= 0")
