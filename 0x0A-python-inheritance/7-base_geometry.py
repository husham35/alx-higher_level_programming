#!/usr/bin/python3
"""Module with BaseGeometry function"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """
        calculates the area of a geometry
        Raises:
            Exception: raised if area computation is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates input (value) and raises exception
        Args:
            name: (str) name of the string
            value: (int) value to be validated
        Raises:
            ValueError: raised if value is <= 0
            TypeError: raised if value is not int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
