#!/usr/bin/python3
"""  module definition of a class square with a private attribute """


class Square:
    """ class definition for square """
    __size = None

    def __init__(self, size):
        """
        Initialization of instance of attributes
        Args: size (int): size of square
        """
        self.__size = size
