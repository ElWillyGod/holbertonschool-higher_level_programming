#!/usr/bin/python3
"""classe square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area Square"""

        return self.__size ** 2

    def __str__(self):
        return str('[Square]'+f"{self.__width}/{self.__heigth}")
