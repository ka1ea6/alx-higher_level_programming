#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as te:
        print("Exception: {}".format(te), file=stderr)
        return False
