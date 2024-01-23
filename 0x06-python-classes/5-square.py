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
        self.__size = size

    def area(self):
        """
        computes area of a square
        :returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter function for size attribute
        :return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function for size attribute
        """
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """
        prints square using # character
        """
        if self.__size > 0:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print("")