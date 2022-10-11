#!/usr/bin/python3

'''module for writing a class that defines a square'''


class Square:
    '''a class representing a square'''

    def __init__(self, size=0):
        ''' initializes a square:

        Args:
            size (int) : size of the square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''method for calculating the area of the square'''

        return self.__size ** 2
