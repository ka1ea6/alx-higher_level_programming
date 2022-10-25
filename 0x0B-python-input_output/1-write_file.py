#!/usr/bin/python3
'''
Module for defining a function that can be used to write to a file
'''


def write_file(filename="", text=""):
    '''Function for writing text to file with name filename'''
    len = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        len = f.write(str(text))
    return len
