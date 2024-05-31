#!/usr/bin/python3
"""CSV data an JSON"""
import csv
import json


def convert_csv_to_json(fileName):
    """cosas"""

    try:
        with open(fileName, 'r') as csvFile:
            csvRader = csv.DictReader(csvFile)
            data = [i for i in csvRader]

        with open('data.json', 'w') as jsonFile:
            json.dump(data, jsonFile)

        return True

    except Exception:

        return False
