#!/usr/bin/python3
"""This function is used to return the list of all
   available attributes and methods of object"""


def lookup(obj):
    return list(dir(obj))
