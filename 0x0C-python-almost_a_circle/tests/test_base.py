#!/usr/bin/python3
"""
Unit Tests for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_base_1_init_with_id(self):
        """Test for initializing Base instance with a specific ID."""
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_base_2_init_without_id(self):
        """Test for initializing Base instances without specifying ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_3_multiple_instances(self):
        """Test for multiple instances of Base with and without ID."""
        b1 = Base()
        b2 = Base()
        b3 = Base(789)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 6)
        self.assertEqual(b3.id, 789)

    def test_base_4_to_json_string(self):
        """Test for the `to_json_string` method."""
        self.assertEqual(Base.to_json_string([]), "[]")
        ld1 = Base.to_json_string([{'id': 21, 'name': 'json'}])
        self.assertEqual(ld1, '[{"id": 21, "name": "json"}]')
        ld2 = Base.to_json_string([{'id': 21, 'name': 'json'},
                                   {'age': 25, 'class': 4}])
        self.assertEqual(ld2, '[{"id": 21, "name": "json"}, '
                         '{"age": 25, "class": 4}]')
        self.assertIsInstance(ld2, str)

    def test_base_5_from_json_string(self):
        """Test for the `from_json_string` method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        ld1 = Base.from_json_string('[{"id": 21, "name": "json"}]')
        self.assertEqual(ld1, [{'id': 21, 'name': 'json'}])
        ld2 = Base.from_json_string('[{"id": 21, "name": "json"}, '
                                    '{"age": 25, "class": 4}]')
        self.assertEqual(ld2, [{'id': 21, 'name': 'json'},
                               {'age': 25, 'class': 4}])
        self.assertIsInstance(ld2, list)


if __name__ == '__main__':
    unittest.main()
