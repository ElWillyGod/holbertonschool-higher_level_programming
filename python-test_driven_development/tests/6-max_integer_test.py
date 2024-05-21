#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def maxt_integer(self):
        self.assertEqual(max_integer[1, 2, 3, 4], 4)
        self.assertEqual(max_integer[1, 4, 2], 4)
        self.assertEqual(max_integer[-1, -2, -3], -1)
