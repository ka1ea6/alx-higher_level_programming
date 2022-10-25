#!/usr/bin/python3
'''Module for defining a function that creates an object
from a JSON file'''

import json


def load_from_json_file(filename):
    '''Function for creating an object from a file containing a
    JSON object'''

    with open(filename, mode="r", encoding="utf-8") as f:
        json_val = f.read()
        return json.loads(json_val)
