#!/usr/bin/python3
"""Defining the function from_json_string"""
import json


def from_json_string(my_str):
    """This function takes my_string which is a
       json serilized string and deserilizes it.
       Args:
           my_str (string): teh string to be converted
       Returns:
           python data structure
    """
    return json.loads(my_str)
