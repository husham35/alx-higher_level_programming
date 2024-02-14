#!/usr/bin/python3
"""
Test suite for square.py `class Square` module
"""
import io
import unittest
from pathlib import Path

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    """Test attributes"""
    def test_initialization_success(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 13)
        self.assertEqual(s2.id, 14)

    def test_initialization_without_arguments(self):

        self.assertRaises(TypeError, Square)


if __name__ == "__main__":
    unittest.main()
