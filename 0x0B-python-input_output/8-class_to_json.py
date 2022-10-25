#!/usr/bin/python3
'''Module for defining a function to serialize an object'''

import json


def class_to_json(obj):
    '''Function to return the serialized object'''
    return json.dumps(obj.__dict__)
