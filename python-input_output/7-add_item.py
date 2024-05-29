#!/usr/bin/python3
"""add all arrguments to a python lisr"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arguments = load_from_json_file("add_item.json")
except FileNotFoundError:
    arguments = []

arguments.extend(sys.argv[1:])
save_to_json_file(arguments, 'add_item.json')
