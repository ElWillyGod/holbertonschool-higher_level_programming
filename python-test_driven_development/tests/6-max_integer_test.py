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
        aa = []
        self.assertEqual(max_integer(aa), None)

    def tests2(self):
        nf = [1, 2, 4]
        self.assertEqual(max_integer(nf), 4)

if __name__ == '__main__':
    unittest.main()
