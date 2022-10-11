#!/usr/bin/python3

'''module for defining a class used as a blueprint for making
    square
'''


class Square:
    ''' A class for defining a square'''

    def __init__(self, size=0):
        '''The method used to instantiate a square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''fuction to get the value of the private property size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''fuction to set the value of the private property size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''function to get the area of the square'''
        return self.__size ** 2
