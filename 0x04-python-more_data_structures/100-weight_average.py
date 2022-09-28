#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = 0
    den = 0
    for i, j in my_list:
        num += (i * j)
        den += j
    return num/den
