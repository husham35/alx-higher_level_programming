#!/usr/bin/python3
"""
module definition of a class square with a private attribute
"""


class Square:
    """ class definition for square """

    # __size = None

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of instance of attribute size to 0
        Args:
            size (int): size of square
            position (int, int): position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter function for the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        :param value: tuple position of the square to be printed
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        prints square using # character
        """
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print("")
