#!/usr/bin/python3
'''Module to define MyList class'''


class MyList(list):
    '''Class that adds a print sorted functionality to list base class'''

    def __init__(self):
        '''Dunder function to initialize class'''
        list.__init__(self)

    def print_sorted(self):
        '''function to print a list sorted in ascending order'''
        clone = self[:]
        clone.sort()
        print(clone)
