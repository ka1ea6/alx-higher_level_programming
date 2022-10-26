#!/usr/bin/python3
'''Module for defining a student class'''


class Student:
    '''class that is used to represent a student'''

    def __init__(self, first_name, last_name, age):
        '''Function to initialize the instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''function to retrieve a dictionary representation
        of a Student instance'''
        instanceCheck = isinstance(attrs, list) and len(attrs) > 0
        if instanceCheck and isinstance(attrs[0], str):
            res = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    res[i] = self.__dict__[i]
            return res
        if isinstance(attrs, list) and len(attrs) == 0:
            return {}
        return self.__dict__
