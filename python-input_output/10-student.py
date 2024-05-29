#!/usr/bin/python3
"""class Student"""


class Student:
    """__init__"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to to_json"""

        direc = self.__dict__
        direcAttrs = dict()

        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return direc

                if i in direc:
                    direcAttrs[i] = direc[i]

            return direcAttrs

        return direc
