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

        if not isinstance(attrs, list):
            return self.__dict__

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """remplasta los directorios"""

        for attr in json:
            self.__dict__[attr] = json[attr]
