#!/usr/bin/python3
"""
Unittest suites for square.py `class Square` module
"""
import unittest
from pathlib import Path

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_with_two_valid_args(self):
        """Test for instance with size and x values."""
        square = Square(1, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 0)

    def test_with_three_valid_args(self):
        """Test for instance with size, x and y values."""
        square = Square(1, 3, 8)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 8)

    def test_size_init_str_size(self):
        """Test for instance with invalid string argument."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_init_str_x(self):
        """Test for instance with invalid string argument for `x`."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "1")

    def test_size_init_str_y(self):
        """Test for instance with invalid string argument for `y`."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, "1")

    def test_size_init_neg_size(self):
        """Test for an instance with negative argument for `size`."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_size_init_neg_x(self):
        """Test for an instance with negative argument for `x`."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -4)

    def test_size_init_neg_y(self):
        """Test for an instance with negative argument for `y`."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 5, -6)

    def test_size_init_zero_size(self):
        """Test for an instance with size argument as 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_str(self):
        """Test for __str__ method of the Square instance."""
        sqr = Square(3, 4, 5, 6)
        sqr_str = "[Square] (6) 4/5 - 3"
        self.assertEqual(str(sqr), sqr_str)

    def test_getter(self):
        """Test for getter method of Square."""
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_setter(self):
        """Test for setter method of Square."""
        square = Square(7)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_with_string(self):
        """Test for setting size with a string value."""
        square = Square(4)
        with self.assertRaises(TypeError):
            square.size = "Hello"

    def test_with_negative(self):
        """Test for setting size with a negative value."""
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -9

    def test_with_zero(self):
        """Test for setting size with zero."""
        square = Square(7)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_with_decimal(self):
        """Test for setting size with a decimal value."""
        square = Square(8)
        with self.assertRaises(TypeError):
            square.size = 4.3

    def test_with_tuple(self):
        """Test for setting size with a tuple value."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = (1, 2)

    def test_with_empty(self):
        """Test for setting size with an empty value."""
        square = Square(9)
        with self.assertRaises(TypeError):
            square.size = ""

    def test_with_none(self):
        """Test for setting size with None."""
        square = Square(3)
        with self.assertRaises(TypeError):
            square.size = None

    def test_with_list(self):
        """Test for setting size with a list value."""
        square = Square(1)
        with self.assertRaises(TypeError):
            square.size = [3, 4]

    def test_with_dict(self):
        """Test for setting size with a dictionary value."""
        square = Square(2)
        with self.assertRaises(TypeError):
            square.size = {"Mont": 3, "Python": 4}

    def test_width(self):
        """Test if width and height are updated when setting size."""
        square = Square(5)
        square.size = 4
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def test_to_dictionary(self):
        """Test for the  `to_dictionary` method of Square."""
        Base._Base__nb_objects = 0

        square = Square(4, 5, 3, 6)
        square_dict = square.to_dictionary()
        expected = {"id": 6, "x": 5, "size": 4, "y": 3}
        self.assertEqual(square_dict, expected)

        square = Square(1, 2, 2, 3)
        square_dict = square.to_dictionary()
        expected = {"id": 3, "x": 2, "size": 1, "y": 2}
        self.assertEqual(square_dict, expected)

        square.update(1, 1, 1, 1)
        square_dict = square.to_dictionary()
        expected = {"id": 1, "x": 1, "size": 1, "y": 1}
        self.assertEqual(square_dict, expected)


class TestSquareCreate(unittest.TestCase):
    """
    Tests to confirm if the create method returns a new square object
    with the attributes updated.
    """

    def test_create_with_1_arg(self):
        """
        Test for `create` method to return an object with
        one attribute updated.
        """
        sqr = Square.create(**{"id": 6})
        self.assertEqual(sqr.id, 6)

    def test_create_with_2_args(self):
        """
        Test for `create` method to return an object with
        two attributes updated.
        """
        sqr = Square.create(**{"id": 2, "size": 3})
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)

    def test_create_with_3_args(self):
        """
        Test for `create` method to return an object with
        three attributes updated.
        """
        sqr = Square.create(**{"id": 4, "size": 5, "x": 6})
        self.assertEqual(sqr.id, 4)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.x, 6)

    def test_create_with_4_args(self):
        """
        Test for `create` method to return an object with
        four attributes updated.
        """
        sqr = Square.create(**{"id": 5, "size": 6, "x": 7, "y": 8})
        self.assertEqual(sqr.id, 5)
        self.assertEqual(sqr.size, 6)
        self.assertEqual(sqr.x, 7)
        self.assertEqual(sqr.y, 8)


class TestSquareSaveToFile(unittest.TestCase):
    """
    Test for the `save_to_file` method of.
    """

    def test_save_to_file_none(self):
        """
        Test for the `save_to_file` method with default.
        """
        Square.save_to_file(None)
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_save_to_file_empty_list(self):
        """
        Test for the `save_to_file` method with nothing.
        """
        Square.save_to_file([])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)
        self.assertIsInstance(objs, list)

    def test_save_to_file_list(self):
        """
        Test for the `save_to_file` method with a list.
        """
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


class TestSquareLoadFromFile(unittest.TestCase):
    """Unit tests for testing the load_from_file method of Square."""

    def setUp(self):
        """
        Removes the Square.json file if it exists.
        """
        if Path("Square.json").is_file():
            Path("Square.json").unlink()

    def test_load_from_file_no_file(self):
        """
        Test for `load_from_file` method with missing Square.json file.
        """
        self.assertFalse(Path("Square.json").is_file())
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_existing_file(self):
        """
        Test for `load_from_file` method with existing Square.json file.
        """
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


if __name__ == "__main__":
    unittest.main()
