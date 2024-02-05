#!/usr/bin/python3
"""
Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes the Rectangle
        Args:
            size: (int) width of the rectangle
        """
        super().integer_validator("size", size)
        self._size = size

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            (int) area of the square
        """
        return self._size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._size, self._size)