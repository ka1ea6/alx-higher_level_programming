#!/usr/bin/python3
'''Module for defining a function that checks if
 an object is an instance of a class'''


def is_kind_of_class(obj, a_class):
    '''Function to test if an object is an instance of a class

    Args:
        @obj: object to be checked
        @a_class: class to be checked
        Return: True if obj is instance of a_class, false otherwise.
    '''

    return isinstance(obj, a_class)
