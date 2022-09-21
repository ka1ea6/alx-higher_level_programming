#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
converted_num = f"{number}"
last_digit = converted_num[-1] if int(number) >= 0 else "-" + converted_num[-1]
string = f"Last digit of {converted_num} is {last_digit} "
if int(last_digit) > 5:
    string = string + "and is greater than 5"
elif int(last_digit) == 0:
    string = string + "and is 0"
else:
    string = string + "and is less than 6 and not 0"
print(string)
