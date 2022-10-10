#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: None")
            return None
        else:
            print("Inside result: {}".format(res))
            return res
