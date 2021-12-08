#!/usr/bin/python3
"""Defining a square"""


class Square:
    """class to compute area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.
        Args:
            size (int): size is a new field it has been initialized to 0.
        """
        self.__size = size
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """funtion to find the area of a square.
        Returns:
            size squared
        """
        return self.__size**2

    @property
    def size(self):
        """Function used to return the value that
           was changed by the size setter function.
        Args:
            value (int): the value to be changed
        Returns:
            the new size
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
