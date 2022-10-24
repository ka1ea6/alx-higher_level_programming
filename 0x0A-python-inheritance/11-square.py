#!/usr/bin/python3
'''
Module to define a class Rectangle that inherits from BaseGeometry
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    class to define a Rectangle
    '''

    def __init__(self, size):
        '''
        Function to instantiate object
        '''
        Rectangle.__init__(self, size, size)
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def __str__(self):
        '''
        Function to return a printable string
        '''
        return "[Square] {}/{}".format(self.__size, self.__size)
