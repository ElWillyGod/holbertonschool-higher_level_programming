#!/usr/bin/python3
"""funtion in read file"""


def read_file(filename=""):
    """open file and read"""

    with open(filename, encoding='UTF8') as arch:
        print(arch.read(), end='')
