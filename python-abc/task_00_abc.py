#!/usr/bin/python3
"""Abstract Class"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """ clase Abstract"""

    @abstractmethod
    def sound(self):
        """sound"""
        pass

class Dog(Animal):
    """sub clase dog"""

    def sound(self):
        """return bark"""

        return "Bark"

class Cat(Animal):
    """sub classe cat"""

    def sound(self):
        """return meow"""

        return "Meow"
