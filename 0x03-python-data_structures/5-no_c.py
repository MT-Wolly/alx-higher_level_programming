#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char not in 'Cc':
            my_string = ''.join(char)
    return my_string
