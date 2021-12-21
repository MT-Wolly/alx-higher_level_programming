#!/usr/bin/python3
"""Defining the class BaseGeometry"""


class BaseGeometry:
    """This is a BaseGeometry class"""

    def area(self):
        """This function is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function is used to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
