#!/usr/bin/python3
'''Module for defining a function used for
 converting a json string to an object'''


import json


def from_json_string(my_str):
    '''Function for converting a string representation of an
    object to the object'''

    return json.loads(my_str)
