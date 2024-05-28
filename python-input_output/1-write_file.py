#!/usr/bin/python3
"""creo que estos comentario ya no son necesarios"""


def write_file(filename="", text=""):
    """open file and retun the numbers of characters written"""

    with open(filename, 'w', encoding='UTF8') as file:
        return file.write(text)
