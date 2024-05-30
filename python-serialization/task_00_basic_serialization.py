#!/usr/bin/python3
"""serialzation"""
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r') as file:
        dataObjet = json.load(file)

    return dataObjet
