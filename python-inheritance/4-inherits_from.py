#!/usr/bin/python3
"""
    inherits from
"""


def inherits_from(obj, a_class):
    """medio mareado"""

    return type(obj) is a_class and not isinstance(obj, a_class)
