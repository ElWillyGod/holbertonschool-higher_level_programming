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
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter to value in height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return:
            perimeter Rectangle
        """

        if (self.__height == 0 or self.__height == 0):
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """imprime el Rectangle"""

        if (self.__width == 0 or self.__height == 0):
            return ""

        rec = []

        for i in range(self.height):
            if i == self.__height - 1:
                rec.append('#' * self.__width)
            else:
                rec.append(('#' * self.__width) + '\n')

        return ("".join(rec))
