#!/usr/bin/python3
"""dragon"""


class SwimMixin:
    """class SwimMixin"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """class FlyMixin"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class dragon"""

    def roar(self):
        print("The dragon roars!")
