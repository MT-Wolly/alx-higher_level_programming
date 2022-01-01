#!/usr/bin/python3
"""
This module contains the Rectangle class and inhgerits from the Base class
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
