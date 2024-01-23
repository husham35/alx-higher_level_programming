#!/usr/bin/python3
"""
module definition of a class square with a private attribute
"""


class Square:
    """ class definition for square """
    __size = None

    def __init__(self, size=0):
        """
        Initialization of instance of attribute size to 0
        Args: size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size > 0:
                self.__size = size
            else:
                raise ValueError('size must be >=0')