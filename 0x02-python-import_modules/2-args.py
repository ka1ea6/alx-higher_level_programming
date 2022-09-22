#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        argPrint = "{0} argument:".format(len(sys.argv) - 1)
    else:
        argPrint =  "0 arguments."
    print(argPrint)
    for i in range(1, len(sys.argv)):
        print("{0}: {1}".format(i, sys.argv[i]))
