#!/usr/bin/python3
"""track of iteration"""


class CountedIterator:
    """countedIterator"""

    def __init__(self, objIter):
        """iterar objeto y implementar contador"""

        self.itera = iter(objIter)
        self.counter = 0

    def get_count(self):
        """geter in conut"""
        return self.counter

    def __next__(self):
        """return next item"""
        self.counter += 1

        try:
            return next(self.itera)
        except StopIteration:
            raise StopIteration
