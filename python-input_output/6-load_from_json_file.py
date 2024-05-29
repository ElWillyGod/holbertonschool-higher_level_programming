#!/usr/bin/python3
"""creates an object from a json file"""


import json


def load_from_json_file(filename):
    """open file and create object"""
    return json.load(open(filename))
