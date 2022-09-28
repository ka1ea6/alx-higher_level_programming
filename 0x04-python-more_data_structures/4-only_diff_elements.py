#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp_1 = set_1.copy()
    temp_1.update(set_2)
    set_1 &= set_2
    temp_1 -= set_1
    return temp_1
