#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    if op != "+" and op != "-" and op != "/" and op != "*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if(op == "+"):
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
        exit(0)
    elif(op == "-"):
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
        exit(0)
    elif(op == "*"):
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
        exit(0)
    elif(op == "/"):
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
        exit(0)
