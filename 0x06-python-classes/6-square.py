#!/usr/bin/python3
'''Module for defining a square'''


class Square:
    '''Class representing a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Function for initializing a square'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = position
        if not isinstance(a, int) or not isinstance(b, int):
             raise TypeError("position must be a tuple of 2 positive integers")
        if a < 0 or b < 0:
             raise TypeError("position must be a tuple of 2 positive integers")
        print(position)

        self.__position = position

    @property
    def size(self):
        '''Function to get the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Function to set the size of the square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Function to get the current position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Function to set the value of the current position'''
        a, b = value
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Function to get the area based on the current size'''
        return self.__size ** 2

    def my_print(self):
        '''Function to print the square with # characters'''

        if self.__size == 0:
            print("")
        else:
            a, b = self.__position
            for _ in range(b):
                print("")
            for i in range(self.__size):
                for _ in range(a):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
