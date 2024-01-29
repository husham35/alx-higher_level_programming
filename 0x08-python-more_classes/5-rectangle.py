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

    def area(self):
        """
        Return the area of the rectangle
        :return: (int) the area of the rectangle
        """
        return self.__width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        :returns: (int) the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Draw string representation of the rectangle with #
        :return: (str) the string representation with #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(('#' * self.width) for _ in range(self.height))

    def __repr__(self):
        """
        String representation of the rectangle object
        :return: (str) the string representation of the rectangle object
        that is compatible with the eval() function
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
