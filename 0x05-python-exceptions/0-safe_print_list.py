#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    i = 0
    try:
        while (i < x):
            print(my_list[i], end="")
            i += 1
            total += 1
    except IndexError:
        print()
        return total
    else:
        print()
        return x
