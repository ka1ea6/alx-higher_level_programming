#!/usr/bin/python3
'''
Module to define a class Rectangle that inherits from BaseGeometry
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    class to define a Rectangle
    '''

    def __init__(self, width, height):
        '''
        Function to instantiate object
        '''
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
