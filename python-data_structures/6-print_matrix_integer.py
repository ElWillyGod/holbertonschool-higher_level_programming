#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None or not matrix:
        return

    for i in matrix:
        if not i:
            continue

        for j in i:
            print("{:d}".format(j), end="")
            print(' ', end='') if j != i[-1] else print()

