#!/usr/bin/python3
'''Module defining a lookup function used to list all attributes 
and methods of an object
'''


def lookup(obj):
    '''Function used to perform lookup on an object'''
    return dir(obj)