#!/usr/bin/python3
'''
Module containing a function for adding new lines after '.' '?' or ':'
'''


def text_indentation(text):
    '''
    Function used to indent the passed text
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # [print(f"{char}", end="") if char not in ['.', '?', ':']
    # else print("\n") for char in text]
    string = ""
    i = 0
    while i < len(text):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            string += text[i]
        else:
            string += text[i] + ('\n' * 2)
            if text[i + 1] == ' ':
                i += 1
        i += 1

    print(string)
