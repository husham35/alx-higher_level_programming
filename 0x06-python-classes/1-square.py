#!/usr/bin/python3
"""  module definition of a class square with a private attribute """


class Square:
    __size = None

    def __init__(self, size):
        self.__size = size
