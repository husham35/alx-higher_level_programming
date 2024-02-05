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
