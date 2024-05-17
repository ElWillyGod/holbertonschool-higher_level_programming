#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    cont = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            cont += 1
        except IndexError:
            break

        print()

        return cont
