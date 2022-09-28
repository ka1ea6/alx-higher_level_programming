#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for i in a_dictionary.keys():
       if a_dictionary[i] is value:
            to_del.append(i)
    for i in to_del:
        del a_dictionary[i]
    return a_dictionary