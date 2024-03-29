#!/usr/bin/python3
"""Module contains a class Rectangle"""


class Rectangle:
    """Rectangle class definition"""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle class
        :param width: (int) width of the rectangle
        :param height: (int) height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        :param value: (int) new width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        :param value: (int) new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
