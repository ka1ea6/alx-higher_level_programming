#!/usr/bin/python3
'''Module defining a function that returns
a JSON representation of an object'''


import json


def to_json_string(my_obj):
    '''Function returning a json representation of an object'''

    return json.dumps(my_obj)
