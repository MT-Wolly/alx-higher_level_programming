#!/usr/bin/python3
""" Module for test Square class """
import unittest
from unittest.mock import patch
from unittest import TestCase
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Testing the Square class methods """

    def setUp(self):
        """ Method initialized for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Testing new square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Testing new square with all attributes """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Testing new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_Base_instance(self):
        """ Testing Square is a Base instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """ Testing Square as a Rectangle instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_incorrect_amount_attr(self):
        """ Testing error raise with no arguments passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attr_1(self):
        """ Testing error raised with no arguments passed """
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attr(self):
        """ Testing to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attr_2(self):
        """ Testing to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attr_3(self):
        """ Testing to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attr_4(self):
        """ Testing to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valid_attr(self):
        """ passing a string value into the method """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valid_attr_2(self):
        """ passing a string value into the method """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valid_attr_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attr(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attr_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attr_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of the area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_area_2(self):
        """ Checking the return value of the area method """
        new = Square(2)
        self.assertEqual(new.area(), 4)

        new = Square(5)
        self.assertEqual(new.area(), 25)

    def test_load_from_file(self):
        """ Testing load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_display(self):
        """ Testing display method implemented"""
        rect_1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Testing display method implemented """
        rect_1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

        rect_1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_3(self):
        """ Testing display method implemented """
        square_1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square_1.display()
            self.assertEqual(str_out.getvalue(), res)


    def test_display_4(self):
        """ Testing display method implemented"""
        square_1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square_1.display()
            self.assertEqual(str_out.getvalue(), res)

        square_1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square_1.display()
            self.assertEqual(str_out.getvalue(), res)

        square_1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Testing string representation return value """
        rect_1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Testing string representation return value """
        rect_1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

        rect_1.id = 1
        rect_1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Testing string representation return value """
        square_1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_2)
            self.assertEqual(str_out.getvalue(), res)

        square_3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Testing string representation return value """
        square_1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(square_1.__str__(), res)


    def test_update(self):
        """ Test update method implemented"""
        square_1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_2(self):
        """ Test update method implemented"""
        square_1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        """ Test update method implemented"""
        square_1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_4(self):
        """ Test update method implemented"""
        square_1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'size': 3, 'y': 5}
        square_1.update(**dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_5(self):
        """ Test update method implemented """
        square_1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            square_1.update(**dic)

    def test_to_dictionary(self):
        """ Testing dictionary method implemented """
        square_1 = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(square_1.size, 1)
        self.assertEqual(square_1.width, 1)
        self.assertEqual(square_1.height, 1)
        self.assertEqual(square_1.x, 2)
        self.assertEqual(square_1.y, 3)
        self.assertEqual(square_1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(square_1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary method implemented """
        square_1 = Square(2, 2, 2)
        res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_1)
            self.assertEqual(str_out.getvalue(), res)

        square_2 = Square(5)
        res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square_2)
            self.assertEqual(str_out.getvalue(), res)

        square_1_dictionary = square_1.to_dictionary()
        square_2.update(**square_1_dictionary)

        self.assertEqual(square_1.width, square_2.width)
        self.assertEqual(square_1.height, square_2.height)
        self.assertEqual(square_1.x, square_2.x)
        self.assertEqual(square_1.y, square_2.y)
        self.assertEqual(square_1.id, square_2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(square_1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string method """
        square_1 = Square(2)
        dict = square_1.to_dictionary()
        json_dict = Base.to_json_string([dict])
        res = "[{}]\n".format(dict.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_json_file(self):
        """ Test Dictionary to JSON string method"""
        square_1 = Square(2)
        dict = square_1.to_dictionary()
        json_dict = Base.to_json_string([dict])
        res = "[{}]\n".format(dict.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), res)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            square_1 = Square(-1)

    def test_create(self):
        """ Test create method implemented """
        dict = {'id': 89}
        square_1 = Square.create(**dict)
        self.assertEqual(square_1.id, 89)

    def test_create_2(self):
        """ Test create method implemented"""
        dict = {'id': 89, 'size': 1}
        square_1 = Rectangle.create(**dict)
        self.assertEqual(square_1.id, 89)
        self.assertEqual(square_1.size, 1)

    def test_create_3(self):
        """ Test create method implemented"""
        dict = {'id': 89, 'size': 1, 'x': 2}
        square_1 = Rectangle.create(**dict)
        self.assertEqual(square_1.id, 89)
        self.assertEqual(square_1.size, 1)
        self.assertEqual(square_1.x, 2)

    def test_create_4(self):
        """ Test create method implemented"""
        dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        square_1 = Rectangle.create(**dict)
        self.assertEqual(square_1.id, 89)
        self.assertEqual(square_1.size, 1)
        self.assertEqual(square_1.x, 2)
        self.assertEqual(square_1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file method implemented"""
        square_1 = Square(5)
        square_2 = Square(8, 2, 5)

        l_input = [square_1, square_2]
        Square.save_to_file(l_input)
        l_output = Square.load_from_file()

        for i in range(len(l_input)):
            self.assertEqual(l_input[i].__str__(), l_output[i].__str__())
