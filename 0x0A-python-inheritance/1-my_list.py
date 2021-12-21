#!/usr/bin/python3
"""Defining print_sorted"""


class MyList(list):
    """This is a class that inherits from built-in list
       Args:
           list (list): the built-in class
    """
    pass

    def print_sorted(self):
        """This function is used to print a list in ascending
           order"""
        self = sorted(self)
        print(self)
