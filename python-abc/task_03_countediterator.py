#!/usr/bin/python3
"""track of iteration"""


class CountedIterator:
    """countedIterator"""

    def __init__(self, objIter):
        """iterar objeto y implementar contador"""

        self.__itera = iter(objIter)
        self.__counter = 0

    def get_count(self):
        """geter in conut"""
        return self.__counter

    def __next__(self):
        """return next item"""
        self.__counter += 1

        try:
            return next(self.__itera)

        except StopIteration:

            raise StopIteration("During handling of the above exception" +
                                ", another exception occurred")
