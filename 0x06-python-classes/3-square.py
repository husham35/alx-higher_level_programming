#!/usr/bin/python3
"""
module definition of a class square with a private attribute
"""


class Square:
    """ class definition for square """
    # __size = None

    def __init__(self, size=0):
        """
        Initialization of instance of attribute size to 0
        Args: size (int): size of square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        computes area of a square
        returns: the current square area.
        """
        return self.__size ** 2
