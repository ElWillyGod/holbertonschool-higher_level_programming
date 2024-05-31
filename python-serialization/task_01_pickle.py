#!/usr/bin/python3
"""pickle"""
import pickle


class CustomObject:
    """objet custom"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print self"""

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize filename"""

        with open(filename, 'wb') as fileText:
            pickle.dump(self, fileText)

    @classmethod
    def deserialize(cls, filename):
        """deserialize filename"""

        try:
            with open(filename, 'rb') as fileText:
                objet = pickle.load(fileText)
        except Exception:
            return None

        return objet
