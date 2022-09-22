#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
    print("{0}".format(dir("./hidden_4(1).pyc")))
