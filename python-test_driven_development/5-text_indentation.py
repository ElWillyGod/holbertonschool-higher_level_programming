#!/usr/bin/python3
"""magin in text"""


from re import L


def text_indentation(text):
    """validaciones"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in ".:?":
        text = (i + "\n\n").join([j.strip(" ") for j in text.split(i)])

    print("{}".format(text), end='')
