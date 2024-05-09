#!/usr/bin/python3
if __name__ == "__main_":
    import sys

    cantArg = len(sys.argv)

    if cantArg == 0:
        print("0 arguments.")
    elif cantArg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cantArg))

    for i in range(1, cantArg + 1):
        print("{}: {}".format(i, sys.argv[i]))
