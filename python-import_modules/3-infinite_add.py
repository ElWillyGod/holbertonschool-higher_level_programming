#!/usr/bin/python3
if __name__ in "__main__":
    import sys

    suma = 0
    for i in range(1, len(sys.argv)):
        suma += int(sys.argv[i])

    print("{}".format(suma))
