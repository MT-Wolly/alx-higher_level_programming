#!/usr/bin/python3
"""Defining Square in class"""


class Square:
    """This is class is to compute the area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.
        Args:
            size (int): size - initialized to 0.
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

    @property
    def size(self):
        """function return to the value that changed by 
            the size setter function.
        Args:
            value (int): value to be changed
        Returns:
              new size
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
