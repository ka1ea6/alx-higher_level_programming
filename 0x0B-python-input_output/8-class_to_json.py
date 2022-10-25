#!/usr/bin/python3
'''Module for defining a function to serialize an object'''


def class_to_json(obj):
    '''Function to return the serialized object'''
    return obj.__dict__
