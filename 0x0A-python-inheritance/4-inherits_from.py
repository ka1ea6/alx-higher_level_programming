#!/usr/bin/python3
'''Module for defining a function that checks if
 an object is instantiated froma class that derives
 from another'''


def inherits_from(obj, a_class):
    '''Function to test if an object is an instance of a class
    that derives from the given class

    Args:
        @obj: object to be checked
        @a_class: class to be checked
        Return: True if obj is instance of a class that derives
        from a_class, false otherwise.
    '''

    return isinstance(obj, a_class) and type(obj).__name__ != a_class.__name__
