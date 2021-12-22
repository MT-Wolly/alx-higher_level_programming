#!/usr/bin/python3
"""Defining the fnction to_json_string"""
import json


def to_json_string(my_obj):
    """This function is used to convert my_obj
       into a string form using json.
       Args:
           my_obj (unknown): the content to be converted
       Returns:
           the string format of my_obj
    """
    return json.dumps(my_obj)
