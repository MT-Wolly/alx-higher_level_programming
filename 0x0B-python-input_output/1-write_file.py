#!/usr/bin/python3
"""Defining the function write_file"""


def write_file(filename="", text=""):
    """This function is used to wriet on
       the filename the content of text.
       Args:
           filename (str): the file
           text (str): the string to be added
       Returns:
           teh number of characters added
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
