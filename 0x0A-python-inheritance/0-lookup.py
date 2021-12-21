#!/usr/bin/python3
"""Function to return the list of available attributes and methods of an object"""


def lookup(obj):
    """This function returns all the list of available
       attributes and methods of object"""
    return list(dir(obj))
