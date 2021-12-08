#!/usr/bin/python3
"""Defining Square in class"""


class Square:
    """class to compute area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.
        Args:
            size (int): size is a field and has been initialized to 0.
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

    def my_print(self):
        """This function is used to print a square in form
        of # using the value given.
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
