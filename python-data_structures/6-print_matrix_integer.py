#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join(format(num) for num in i))
