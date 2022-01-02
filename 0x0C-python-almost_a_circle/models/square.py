#!/usr/bin/python3
"""
This module contains the square class that inherits from the rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Defining the square class"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing the variables"""
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ Special string representation method"""
        str_square = "[Square]"
        str_id = " ({}) ".format(self.id)
        str_xy = "{}/{} -".format(self.x, self.y)
        self_wh = "{}/{}".format(self.width,self.height)

        return str_square + str_id + str_xy + str_wh


    @property
    def size(self):
        """ size getter"""
        return self.width


    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value
    

    def __str__(self):
        """ str special method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

