#!/usr/bin/python3
"""
Unit Test for maximum integer in a list
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for the `max_integer` function"""

    def test_max_ordered_list(self):
        """case when the maximum value is an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_unordered_list(self):
        """case when the maximum value is in an unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_beginning(self):
        """case when the maximum value is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """case when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """case when the list contains a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """case when the list contains only floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """case when the list contains a mixture of ints and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """case when the input is a string."""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """case when the list contains strings."""
        self.assertEqual(max_integer(["Python", "is", "cool"]), "Python")

    def test_empty_string(self):
        """case when the input is an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_neg_integers(self):
        """case when the list contains negative integers."""
        self.assertEqual(max_integer([-10, -5, -7, -2]), -2)

    def test_duplicate_max_value(self):
        """case when the list contains duplicate maximum values."""
        self.assertEqual(max_integer([3, 2, 4, 2, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
