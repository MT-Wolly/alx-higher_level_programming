#!/usr/bin/python3
"""Defining the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """This function takes the filename and
       uses json to deserilize the content.
       Args:
           filename (str): the file
       Returns:
           the deseilized content of file
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
