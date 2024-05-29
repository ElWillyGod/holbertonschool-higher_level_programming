#!/usr/bin/python3
"""to JSON representation a text file"""


import json


def save_to_json_file(my_obj, filename):
    """open an dump"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
