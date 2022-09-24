#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_init(tuple_a)
    tuple_b = tuple_init(tuple_b)
    c, d = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return (c, d)


def tuple_init(tuple_c):
    while(len(tuple_c) < 2):
        tuple_c = tuple_c + (0,)
    a, b = tuple_c[0], tuple_c[1]
    return (a, b)
