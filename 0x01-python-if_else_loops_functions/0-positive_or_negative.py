#!/usr/bin/python3
import random
number = random.randint(-10, 10)
string = "{:d} is ".format(number)
if number > 0:
    string = string + "positive"
elif number == 0:
    string = string + "zero"
else: 
    string = string + "negative"
print(f"{string}")