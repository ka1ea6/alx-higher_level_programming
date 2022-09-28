#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    a = {x for x in my_list}
    for i in a:
        sum += i
    return sum
