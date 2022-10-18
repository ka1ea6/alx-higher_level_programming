#!/usr/bin/python3
'''
Module containing function for printing a square
'''


def print_square(size):
    '''
    Function for printing a square with '#' character    
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    string = ""

    string += (("#" * size) + '\n') * (size - 1)
    string += "#" * size
    
    print(string)