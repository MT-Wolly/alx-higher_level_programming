#!/usr/bin/python3
"""Defining class Student"""


class Student:
    """This is a class called Student"""

    def __init__(self, first_name, last_name, age):
        """This is function initilizes the class Student.
           Args:
               first_name (str): the first name
               last_name (str): the last name
               age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function is used to retreive the dictionary
           representation of student instance
        """
        return self.__dict__
