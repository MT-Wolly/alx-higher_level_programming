#!/usr/bin/python3
"""Defining the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """This function checks if obj is instance or
       inheritance of a_class
       Args:
           obj (class): the class to be checked
           a_class (class): the class to compare to
       Returns:
           if they are instances then true else false
    """
    if isinstance(obj, a_class):
        return True
    return False
