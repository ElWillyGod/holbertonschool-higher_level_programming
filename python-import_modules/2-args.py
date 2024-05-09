#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cantArg = len(sys.argv)

    if cantArg == 1:
        print("0 arguments.")
    elif cantArg == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(cantArg - 1))

    for i in range(1, cantArg + 1):
        print("{}: {}".format(i, sys.argv[i]))
