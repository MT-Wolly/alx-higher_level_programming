#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            conv = 32
        else:
            conv = 0
        print("{:c}".format(ord(str[i]) - conv), end='')
    print()
