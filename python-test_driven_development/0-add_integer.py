#!/usr/bin/python3
"""add integer"""


def add_integer(a, b=98):
    """
    esto da error si no son int o float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
