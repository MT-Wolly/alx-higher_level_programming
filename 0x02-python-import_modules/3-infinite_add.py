#!/usr/bin/python3
"""This program prints all the results of the addition of all the arguments"""
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
