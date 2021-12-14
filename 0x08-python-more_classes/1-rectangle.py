#!/usr/bin/python3
"""Defining a Rectangle"""


class Rectangle:
    """This is used to create an instance Rectangle"""

    def __init__(self, width=0, height=0):
        """This function is used to initialize the instance.
           Args:
               width (int): width of rectangle
               height (int): height of rectangle
        """
        if not(isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        elif not(isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This function is used to change the value of
           private attribute width to value given in setter
           function.
           Args:
               value (int): new value of width
           Returns:
               new value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This function is used to change the value of
           private attribute height to value given in setter
           function.
           Args:
               value (int): the new value of height
           Returns:
               new value
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
