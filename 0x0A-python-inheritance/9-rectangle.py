#!/usr/bin/python3
"""Defining the class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle class"""

    def __init__(self, width, height):
        """This class is used to initiate the class rectangle.
           Args:
               width (int): the width of rectangle
               height (int): teh height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This function finds the area of a rectangle.
           Return: area of rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """This function is used to return a string format"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
