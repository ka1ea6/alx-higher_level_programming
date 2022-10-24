#!/usr/bin/python3
'''Module to define a function to check if
an objec is an exact instance of a class'''


def is_same_class(obj, a_class):
    '''Function to test if an object is an instance of a class

    Args:
        @obj: object to be checked
        @a_class: class to be checked
        Return: True if class is exact instance, false otherwise.
    '''
    return (isinstance(obj, a_class) and isinstance(obj, a_class.__bases__))
