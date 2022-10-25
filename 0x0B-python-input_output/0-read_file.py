#!/usr/bin/python3
'''
Module for defining a function to read a text file and print it to stdout
'''


def read_file(filename=""):
    '''Function to open a file with name filename and
    print the lines to stdout'''

    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    