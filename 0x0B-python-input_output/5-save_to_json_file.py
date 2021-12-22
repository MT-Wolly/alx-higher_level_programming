#!/usr/bin/python3
"""Defining the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """This function serilizes my_obj and addes it to
       filename.
       Args:
           my_obj (unknown): the content to be serialized
           filename (str): teh file the content will be added to
    """
    with open(filename, "w", encoding='utf-8') as f:
        return json.dump(my_obj, f)
