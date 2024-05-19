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
        __position (int): position in square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): tamanio del cuadrado.
            position (int, int): position in square tuple positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Returns:
            retun size Square
        """
        return (self.__size)

    @property
    def position(self):
        """
        Returns:
            return in the position square
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): tamanio del cuadrado
        """

        if (type(value) is not int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """setter the position Square
        primeto ver si es una tupla de 2
        luego ver si son enteros
        y por ultimo verificar si son positive
        """

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(j >= 0 for j in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Returns:
            return the area square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square"""

        if (self.__size == 0):
            print("")
            return

        [print("") for a in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]
            print("")
