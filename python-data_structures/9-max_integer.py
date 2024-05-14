#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    num = my_list[0]
    for i in range(len(my_list)):
        if num < my_list[i]:
            num = my_list[i]

    return num
