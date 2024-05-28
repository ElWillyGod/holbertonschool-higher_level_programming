#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    with open(filename, encoding='UTF8') as file:
        return file.write(text)
