#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    a ver
    """


    def tests(self):
        """dasd"""
        self.assertEqual(max_integer([]), None)

    def tests2(self):
        """da"""
        self.assertEqual(max_integer([1, 2, 4]), 4)
        self.assertEqual(max_integer([4, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1, -2, 4]), 4)


if __name__ == '__main__':
    unittest.main()
