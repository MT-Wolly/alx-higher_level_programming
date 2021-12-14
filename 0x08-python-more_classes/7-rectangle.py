#!/usr/bin/python3
"""Defining Rectangle"""


class Rectangle:
    """This is used to create an instance of a Rectangle.
       It has one public attribute.
    Attributes:
        number_of_instances (int): counts the number of
        instances created and deleted
        print_symbol (str): prints desired symbol when
        instance or class is called
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
               value (int): new value of height
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

    def area(self):
        """This function is used to return the product
           of height and width
        """
        return self.__width * self.__height

    def perimeter(self):
        """This function is used to return the sum
           of all sides of the rectangle
        """
        if ((self.__width == 0) or (self.__height == 0)):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """This function is used to return the string
           representation of the rectangle in the form
           of print_symbol
        """
        new_string = ""
        if ((self.__width == 0) or (self.__height == 0)):
            return new_string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_string += str(self.print_symbol)
                new_string += "\n"
            return new_string.rstrip()

    def __repr__(self):
        """This function is used to return the string
           representation of the rectangle
        """
        return f'Rectangle(' + str(self.__width) + ','\
            + str(self.__height) + ')'

    def __del__(self):
        """This function is used to delete instances of
           of a class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
