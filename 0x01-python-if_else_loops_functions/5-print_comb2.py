#!usr/bin/python3
for i in range(100):
    if i != 99:
        print("{:2d}, ".format(i), end="")
    else:
        print("{:2d}".format(i))
        break