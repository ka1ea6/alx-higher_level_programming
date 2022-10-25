#!/usr/bin/python3
'''Module for defining a student class'''


class Student:
    '''class that is used to represent a student'''

    def __init__(self, first_name, last_name, age):
        '''Function to initialize the instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''function to retrieve a dictionary representation
        of a Student instance'''
        return self.__dict__
