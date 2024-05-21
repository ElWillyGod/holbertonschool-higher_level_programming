#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """xd"""

    def maxt_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([9, 4, 2]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4]), 4)
