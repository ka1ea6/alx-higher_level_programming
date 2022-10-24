#!/usr/bin/python3
'''Module for defining a class BaseGeometry'''


class BaseGeometry:
    '''
    Empty class.
    '''

    def area(self):
        '''
        Function to calculate area that is not implemented yet
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Function to valudate whether or not value is an int and is
        greater than 0
        Args:
            @self: reference to the instance
            @name: name of the value to be checked
            @value: value to be checked
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
