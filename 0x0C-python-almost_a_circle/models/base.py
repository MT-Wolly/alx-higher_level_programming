#!/usr/bin/python3
"""This is a module that contains the base class"""
import json
import csv
import os.path


class Base:
    """Defining a Base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """This function initializes instances of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """ method to convert list to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)




