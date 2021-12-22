#!/usr/bin/python3
"""Definging the function class_to_json"""


def class_to_json(obj):
    """This function returns the dictonary description
       of data structures for serilization
       Args:
           obj (class): the class
       Returns:
           The attributes of the class obj
    """
    return obj.__dict__
