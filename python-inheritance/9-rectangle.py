#!/usr/bin/python3
"""empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """area in Rectangle"""

        return self.__width * self.__heigth

    def __str__(self):
        """print format [Rectangle] 3/5"""

        return str(f"[Rectangle] {self.__width}/{self.__heigth}")
