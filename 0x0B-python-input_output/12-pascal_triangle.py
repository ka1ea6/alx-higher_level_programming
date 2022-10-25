#!/usr/bin/python3
'''Module for defining a function for getting the
pascal's triangle'''


def pascal_triangle(n):
    '''Function to get list of list of integers representing
    the pascal's triangle of n'''

    res = [[1], [1, 1]]

    if n <= 0:
        return []
    if n == 1:
        return res[0:1]
    elif n == 2:
        return res

    for i in range(1, n - 1):
        new_row = [1]
        for j in range(1, i + 1):
            new_row.append(res[i][j - 1] + res[i][j])
            continue
        new_row.append(1)
        res.append(new_row)

    return res
