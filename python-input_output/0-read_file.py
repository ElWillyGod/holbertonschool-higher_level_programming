#!/usr/bin/python3
"""funtion in read file"""


def read_file(filename=""):

    with open(filename, encoding='UTF8') as arch:
        print(arch.read(), end='')
