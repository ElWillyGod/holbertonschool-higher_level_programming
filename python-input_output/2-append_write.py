#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """open fila and escribir al final de un archivo"""

    with open(filename, 'a', encoding='UTF8') as file:
        return file.write(text)
