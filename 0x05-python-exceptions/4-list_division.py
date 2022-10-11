#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        while True:
            try:
                if not my_list_1[i] or not my_list_2[i]:
                    raise IndexError
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                my_list1_type_check = isinstance(my_list_1[i], int)
                my_list2_type_check = isinstance(my_list_2[i], int)
                if not my_list1_type_check or not my_list2_type_check:
                    raise TypeError
                res.append(my_list_1[i]/my_list_2[i])
            except IndexError:
                print("out of range")
                res.append(0)
            except ZeroDivisionError:
                print("division by 0")
                res.append(0)
            except TypeError:
                print("wrong type")
                res.append(0)
            finally:
                break
    return res
