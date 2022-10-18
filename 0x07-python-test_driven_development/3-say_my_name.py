#!/usr/bin/python3
'''
Module containing the function to print the full name of users
'''
def say_my_name(first_name, last_name=""):
    '''
    Funciton to print the full name based on the given 
    first and last name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name,str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))