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
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
