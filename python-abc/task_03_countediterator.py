#!/usr/bin/python3
"""track of iteration"""


class CountedIterator:
    """countedIterator"""

    def __init__(self, objIter):
        """iterar objeto y implementar contador"""

        self.__itera = iter(objIter)
        self.__counter = 0
        self.__maxtCount = len(objIter)

    def get_count(self):
        """geter in conut"""
        return self.__counter

    def __next__(self):
        """return next item"""

        if (self.__maxtCount <= self.__counter):
            raise StopIteration

        self.__counter += 1

        return next(self.__itera)
