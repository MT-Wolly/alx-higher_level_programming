#!/usr/bin/python3
"""
This module contains the Rectangle class and inherits from the Base class
"""
from models.base import base


class Rectangle(Base):
    """
    Defining a rectangle class with private instance attributes,     each with its own public getter and setter. 
"""
    def __init__(self, width, height, x =0, y=0, id=None):
        """Initializes instances of the class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self.value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """x setter"""
        return selx.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """y setter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """
        function that returns the area of the rectangle object
        """
    

    def display(self):
        """
        Function that prints in stdout the rectangle instance 
        with the character #
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle = rectangle + (" " * self.x)
            rectangle = rectangle + ("#" * self.width) + "\n"
        
        print(rectangle, end='')


    def __str__(self):
        """
        function to define the string representation 
        """
        str_rectangle = "[Rectangle]"
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """
        Function to update the public method by assigning 
        arguments and key/value arguments to attributes
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        """ 
        Method that returns a dictionary representation of a         rectangle 
        """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
