#!/usr/bin/python3
'''Python script to find the peak in a 
list of unordered integers'''


def find_peak(list_of_integers):
    '''Function to find the peak in the passed list of 
    unordered integers'''

    if list_of_integers is None or list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers)
    mid = ((high - low) // 2) + low

    if high == 1:
        return list_of_integers[0]

    if high == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
