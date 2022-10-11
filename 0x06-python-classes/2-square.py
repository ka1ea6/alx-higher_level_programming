#!/usr/bin/python3
'''A Module containing a class that defines
a square based on the passed size'''


class Square:
    '''a class that defines a square based on the passed size'''

    def __init__(self, size=0):
        '''Initializes a new Square.

        Args:
            size (int): The size of the new square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
