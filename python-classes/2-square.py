#!/usr/bin/python3
"""
    Square:
        ss
"""


class Square:
    """__init__
    metodo de inicio

    Attributes:
        __size (int): The size of square(private attribute).
    """

    def __init__(self, size):

        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
