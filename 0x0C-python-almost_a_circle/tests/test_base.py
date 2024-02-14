#!/usr/bin/python3
"""
Unit Tests for Base class
"""

import sys
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_init_with_id(self):
        """Test for initializing Base instance with a specific ID."""
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_without_id(self):
        """Test for initializing Base instances without specifying ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)

    def test_multiple_instances(self):
        """Test for multiple instances of Base with and without ID."""
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)

    def test_to_json_string(self):
        """Test for the `to_json_string` method."""
        self.assertEqual(Base.to_json_string([]), '[]')
        load_one = Base.to_json_string([{'id': 21, 'name': 'json'}])
        self.assertEqual(load_one, '[{"id": 21, "name": "json"}]')
        load_two = Base.to_json_string([
            {'id': 21, 'name': 'json'}, {'age': 25, 'class': 4}
        ])
        self.assertEqual(load_two, '[{"id": 21, "name": "json"}, '
                         '{"age": 25, "class": 4}]')
        self.assertIsInstance(load_two, str)

    def test_from_json_string(self):
        """Test for the `from_json_string` method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        load_one = Base.from_json_string('[{"id": 21, "name": "json"}]')
        self.assertEqual(load_one, [{'id': 21, 'name': 'json'}])
        load_two = Base.from_json_string('[{"id": 21, "name": "json"}, '
                                         '{"age": 25, "class": 4}]')
        self.assertEqual(load_two, [
            {'id': 21, 'name': 'json'}, {'age': 25, 'class': 4}
        ])
        self.assertIsInstance(load_two, list)




if __name__ == '__main__':
    unittest.main()
