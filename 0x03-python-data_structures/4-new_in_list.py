#!/usr/bin/python3

def new_in_list(my_list, idx, element):

"""Function to replace element at a particular index in a copy list"""

    if idx < 0:
        return (my_list)

    elif idx >= len(my_list) - 1:
        return (my_list)

    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
