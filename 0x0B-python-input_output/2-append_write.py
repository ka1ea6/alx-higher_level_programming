#!/usr/bin/python3
'''Module for defining a function that can append to a file'''


def append_write(filename="", text=""):
    '''Function to append to a file the given text'''

    len = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        len = f.write(text)
    return len
