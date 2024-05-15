#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maxInt = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if j == maxInt:
            return i
