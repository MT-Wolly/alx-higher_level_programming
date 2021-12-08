#!/usr/bin/python3
"""Defining Square in a class"""


class Square:
    """This is class is to compute area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.
        Args:
            size (int): size is a new field and it has been initialized to 0.
        """
        self.__size = size
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """This funtion is used to find the area of square.
        Returns:
            size squared
        """
        return self.__size**2
