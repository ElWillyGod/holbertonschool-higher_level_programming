#!/usr/bin/python3
"""creo que estos comentario ya no son necesarios"""


def write_file(filename="", text=""):

    with open(filename, encoding='UTF8') as file:
        return len(file.readlines())
