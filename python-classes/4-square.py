#!/usr/bin/python3
"""
    Square:
        ss
"""


import re


class Square:
    """__init__
    metodo de inicio

    Attributes:
        __size (int): The size of square(private attribute).
    """

    def __init__(self, size=0):
        """
        Args:
            size (int): tamanio del cuadrado.
        """
        self.size = size

    @property
    def size(self):
        """
        Returns:
            retun size Square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): tamanio del cuadrado
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns:
            return the area square
        """
        return self.__size ** 2
