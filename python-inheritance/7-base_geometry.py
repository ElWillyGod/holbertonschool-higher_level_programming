#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raise"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
