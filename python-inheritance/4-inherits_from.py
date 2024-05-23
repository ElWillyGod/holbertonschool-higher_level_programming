#!/usr/bin/python3
"""
    inherits from
"""


def inherits_from(obj, a_class):
    """medio mareado"""

    return type(obj) is not a_class and isinstance(obj, a_class)
