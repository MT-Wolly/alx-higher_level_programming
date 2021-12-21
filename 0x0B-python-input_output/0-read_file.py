#!/usr/bin/python3
"""Defining the function read_file"""


def read_file(filename=""):
    """This function takes an argument filename
       which is a file and reads its contents to
       standard output.
       Args:
           filename (str): name of a file
    """
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
