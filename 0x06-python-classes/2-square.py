#!/usr/bin/python3
'''A Module containing a class that defines
a square based on the passed size'''


class Square:
    '''a class that defines a square based on the passed size'''

    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
            return
        except ValueError:
            print("size must be >= 0")
            return
