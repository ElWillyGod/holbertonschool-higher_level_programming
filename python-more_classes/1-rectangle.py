#!/usr/bin/python3
"""class Rectangule"""


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """ metodo de inico"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Return:
            width
        """
        return self.__width

    @property
    def height(self):
        """
        Return:
            height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """seter to value in Rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter to value in height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
