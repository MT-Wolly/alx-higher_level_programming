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
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
