#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class definition that represents a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle object
        Args:
            width: (int) width of the rectangle
            height: (int) height of the rectangle
            x: (int) x coordinate of the rectangle
            y: (int) y coordinate of the rectangle
            id: (int) unique id of the rectangle
        """
        self.validate_attribute('width', width)
        self.validate_attribute('height', height)
        self.validate_attribute('x', x)
        self.validate_attribute('y', y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # *************************** getters ***************************
    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    # *************************** setters ***************************
    @width.setter
    def width(self, value):
        """setter for width"""
        self.validate_attribute('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        self.validate_attribute('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x"""
        self.validate_attribute('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y"""
        self.validate_attribute('y', value)
        self.__y = value

    # *********************** validator for attributes *******************
    @staticmethod
    def validate_attribute(name, value):
        """
        Validator for attributes
        Args:
            name: (str) name of the attribute
            value: (int) value of the attribute

        Returns:
            ValueError: if value is not valid
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            err_msg = f"{name} must be an integer"
            raise TypeError(err_msg)

        if name in {"width", "height"} and value <= 0:
            err_msg = f"{name} must be > 0"
            raise ValueError(err_msg)

        if name in {"x", "y"} and value < 0:
            err_msg = f"{name} must be >= 0"
            raise ValueError(err_msg)

    def area(self):
        """
        Returns the area of the rectangle
        Returns: the computed area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle on the screen using `#` character
        Returns: nothing
        """
        print("\n" * self.__y +
            "\n".join(" " * self.__x + "#" * self.__width
                for i in range(self.__height)))

    def __str__(self):
        """
        Overrides the __str__ method
        returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                    self.__class__.__name__, self.id, self.__x, self.__y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Displays the rectangle on the screen using `#` character
         while taking care of x and y
        Args:
            *args: sets positional arguments in the order of
            id, width, height, x, and y
            **kwargs: in case no args are provided, defaults to kwargs
        Returns: nothing
        """
        try:
            if args:
                attrs = ("id", "width", "height", "x", "y")
                for idx, arg in enumerate(args):
                    setattr(self, attrs[idx], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key.lower(), value)
        except (IndexError, AttributeError):
            return

    def to_dictionary(self):
        """
        String representation of the  triangle
        Returns: dictionary representation of the rectangle
        """
        d = {
            "x": self.x,
            "width": self.width,
            "id": self.id,
            "height": self.height,
            "y": self.y
        }
        return d
