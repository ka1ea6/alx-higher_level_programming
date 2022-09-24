#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = my_list[:]
    new_list.sort(reverse=True)
    return new_list[0]
