#!/usr/bin/python3
def uppercase(str):
    strUpper = ""
    for i in range(len(str)):
        if (ord(str[i]) > 96  and ord(str[i]) < 123):
            strUpper = strUpper + chr(ord(str[i]) - 32)
        else: 
            strUpper = strUpper + chr(ord(str[i]))
    print(f"{strUpper}")