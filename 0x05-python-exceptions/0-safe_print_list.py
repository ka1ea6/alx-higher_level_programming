#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while(my_list[i] and i < x):
            i += 1
        for j in range(i):
            print("{0}".format(my_list[j]), end="")
        print("")
        return int(i)

    except IndexError:
        for j in range(i):
            print("{0}".format(my_list[j]), end="")
        print("")
        return int(i)
