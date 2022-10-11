#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        j = 0
        while(my_list[i - 1] and i < x):
            i += 1
        ints = []
        for k in range(i):
            if isinstance(my_list[k], int):
                ints.append(my_list[k])
                j += 1
        for o in range(j):
            print("{:d}".format(ints[o]), end="")
        print("")
        return int(j)
    except IndexError:
        i -= 1
        ints = []
        for k in range(i):
            if isinstance(my_list[k], int):
                ints.append(my_list[k])
                j += 1
        for o in range(j):
            print("{:d}".format(ints[o]), end="")
        raise
