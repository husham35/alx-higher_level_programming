#!/usr/bin/python3
"""
Square class model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class represents a square
    Inherited Attributes:
        id
        __weight        __height
        __x             __y
    Class Attributes:
        size
    Inherted Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object
        Args:
            size: (int) the size of the square
            x: (int) the x position of the square
            y: (int) y position of the square
            id: a unique id for the square
        """
        self.validate_attribute("width", size)
        self.validate_attribute("x", x)
        self.validate_attribute("y", y)
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the
        Returns: (int) the size of the length of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value: (int) the size of the square to be set
        Returns: nothing
        """
        self.validate_attribute("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method
        return: prints [Square] (<id>) <x>/<y> - <size>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes
        Args:
            *args: list of positional arguments to update
            **kwargs: dictionary of keyword arguments to update
        Returns: nothing
        """
        try:
            if args:
                attrs = ["id", "size", "x", "y"]
                for x, arg in enumerate(args):
                    setattr(self, attrs[x], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        except (IndexError, AttributeError):
            return

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square
        Returns: the dictionary representation of the square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
