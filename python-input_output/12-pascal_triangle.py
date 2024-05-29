#!/usr/bin/python3
"""return triangle pascal"""


def pascal_triangle(n):
    """return pascal_triangle"""

    if n <= 0:
        return []

    trian = [[1]]


