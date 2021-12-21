#!/usr/bin/python3
"""Defining Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class called Square"""

    def __init__(self, size):
        """This function is used to initialize a square
           Args:
               size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(width=size, height=size)

    def area(self):
        """This function is used to find the area of a square
           Returns: area of a sqaure
        """
        return self.__size**2
