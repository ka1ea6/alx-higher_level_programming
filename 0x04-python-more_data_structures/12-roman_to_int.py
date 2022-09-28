#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    sum = 0
    last = 0
    for i in roman_string[::-1]:
        if last <= dict[i]:
            sum += dict[i]
        else:
            sum -= dict[i]
        last = dict[i]
    return sum
