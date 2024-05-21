#!/usr/bin/python3
""" divide los elemento la matriz segun un numero"""


def matrix_divided(matrix, div):
    """muchas cosas"""
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(i, list) for i in matrix)
        or not all((isinstance(num, int) or isinstance(num, float))
                   for num in [k for i in matrix for k in i])):
        raise TypeError("matrix must be a "
                        "matrix (list of lists) of integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda i: round(i / div, 2), j)) for j in matrix])
