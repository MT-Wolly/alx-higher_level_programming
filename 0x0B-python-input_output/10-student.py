#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for i_atr in range(len(attrs)):
                for s_atr in obj:
                    if attrs[i_atr] == s_atr:
                        d_list[s_atr] = obj[s_atr]
            return d_list

        return obj
