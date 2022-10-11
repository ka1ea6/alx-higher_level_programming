#!/usr/bin/python3
'''Module for defining a square class'''


class Square:
    '''Class for representing squares'''

    def __init__(self, size=0):
        '''Funtion to instantiate square class'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''Funtion to get the current size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Function to set the size of the square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Function to return the area for current set size'''

        return self.__size ** 2

    def my_print(self):
        '''Function to print a square with the # character'''

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
