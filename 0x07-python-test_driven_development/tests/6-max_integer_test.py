#!/usr/bin/python3
"""
Unit Test for maximum integer in a list
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_max_in_ol(self):
        """case when the maximum value is in an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_ul(self):
        """case when the maximum value is in an unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_start(self):
        """case when the maximum value is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty(self):
        """case when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_single_item(self):
        """case when the list contains a one item."""
        self.assertEqual(max_integer([9]), 9)

    def test_floats(self):
        """case when the list contains only floats."""
        self.assertEqual(max_integer([-9.03, 7.30, 99.19, 10.2, 1.10]), 99.19)

    def test_ints_floats(self):
        """case when the list contains a mixture of ints and floats."""
        self.assertEqual(max_integer([12.59, 1.5, 8, -15, 2]), 12.59)

    def test_neg_ints(self):
        """case when the list contains negative integers."""
        self.assertEqual(max_integer([-9, -5, -3, -1]), -1)

    def test_dup_max_values(self):
        """case when the list contains duplicate maximum values."""
        self.assertEqual(max_integer([1, 2, 6, 2, 5, 6]), 6)

    def test_string(self):
        """case when the input is a string."""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """case when the list contains strings."""
        self.assertEqual(max_integer(["Python", "is", "cool"]), 'is')

    def test_empty_str(self):
        """case when the input is an empty string."""
        self.assertEqual(max_integer(""), None)




if __name__ == '__main__':
    unittest.main()
