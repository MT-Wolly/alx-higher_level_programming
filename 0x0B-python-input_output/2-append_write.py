#!/usr/bin/python3
"""Defining the function append_write"""


def append_write(filename="", text=""):
    """This function is used to write
       the end of a filename the content of text.
       Args:
           filename (str): the file
           text (str): the string to be appended
       Returns:
           the number of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
