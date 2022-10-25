#!/usr/bin/python3
'''Module for defining a function that
writes an object to a text file using JSON representation'''


import json


def save_to_json_file(my_obj, filename):
    '''Function to save the contents of my_obj represented as a
    JSON sting to filename'''

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
