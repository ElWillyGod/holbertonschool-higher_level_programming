#!/usr/bin/python3
"""shape class"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """area and perimeter"""

    @abstractmethod
    def area(self):
        """area shape"""

        pass

    @abstractmethod
    def perimeter(self):
        """perimeter fun"""

        pass


class Circle(ABC):
    """class Circle"""

    def __init__(self, radius):
        """init class"""

        self.__radius = abs(radius)

    def area(self):
        """area return"""

        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """perimeter circle"""

        return 2 * math.pi * self.__radius


class Rectangle(ABC):
    """Rectangle"""

    def __init__(self, width, height):
        """init seter"""

        self.__width = width
        self.__heigth = height

    def area(self):
        """area"""
        return self.__width * self.__heigth

    def perimeter(self):
        """perimeter"""
        return 2 * (self.__width + self.__heigth)


def shape_info(shape):
    """print info"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
