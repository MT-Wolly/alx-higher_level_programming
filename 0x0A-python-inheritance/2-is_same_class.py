#!/usr/bin/python3
"""Defining the function is_same_object"""


def is_same_class(obj, a_class):
    """This function checks if object is instance of
       a class
       Args:
           obj (class): the object to be compared
           a_class (class): the class to be compared to
       Returns:
           True: if instance is true, else false
    """
    if type(obj) is a_class:
        return True
    return False
