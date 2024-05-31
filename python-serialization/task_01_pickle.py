#!/usr/bin/python3
"""pickle"""
import pickle


class CustomObject:
    """objet custom"""

    def __init__(self, name, age, is_student):
        self.__name__ = name
        self.__age__ = age
        self.__is_student__ = is_student

    def display(self):
        """print self"""

        print(f"Name: {self.__name__}")
        print(f"Age: {self.__age__}")
        print(f"Is Student: {self.__is_student__}")

    def serialize(self, filename):
        """serialize filename"""

        with open(filename, 'wb+') as fileText:
            pickle.dump(self, fileText)

    @classmethod
    def deserialize(cls, filename):
        """deserialize filename"""

        objet = None
        try:
            with open(filename, 'rb') as fileText:
                objet = pickle.load(fileText)
        except Exception:
            return None

        return objet
