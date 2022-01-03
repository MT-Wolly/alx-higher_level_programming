#!/usr/bin/python3
""" This module is used for testing the Rectangle class """
import unittest
from unittest.mock import patch
from io import StringIO
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ class Module to test Rectangle class """

    def setUp(self):
        """ Method invoked for each testcase """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Testing new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """ Testing new rectangle with all attributes """
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Testing new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Testing Rectangle as a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 argument passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no argument passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valid_attr(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valid_attr_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valid_attr_3(self):
        """ Testing passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valid_attr_4(self):
        """ Testing passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attr(self):
        """ Testing passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Testing passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attr_2(self):
        """ Testing passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attr_3(self):
        """ Testing passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Testing the return value of area method """
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Testing the return value of area method """
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Testing the return value of area method """
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Testing the display method """
        rect_1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Testing the display method """
        rect_1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

        rect_1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Testing the string representation return value """
        rect_1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Testing the string representation return value """
        rect_1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

        rect_1.id = 1
        rect_1.width = 7
        rect_1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Testing the string representation return value """
        rect_1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

        rect_2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_2)
            self.assertEqual(str_out.getvalue(), res)

        rect_3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Testing the string representation return value """
        rect_1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(rect_1.__str__(), res)

    def test_display_3(self):
        """ Testing display method implemented"""
        rect_1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Testing display method implemented """
        rect_1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

        rect_1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

        rect_1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect_1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Testig the dictonary method implemented """
        rect_1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_1.x, 3)
        self.assertEqual(rect_1.y, 4)
        self.assertEqual(rect_1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rect_1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary method implemented """
        rect_1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_1)
            self.assertEqual(str_out.getvalue(), res)

        rect_2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect_2)
            self.assertEqual(str_out.getvalue(), res)

        rect_1_dictionary = rect_1.to_dictionary()
        rect_2.update(**rect_1_dictionary)

        self.assertEqual(rect_1.width, rect_2.width)
        self.assertEqual(rect_1.height, rect_2.height)
        self.assertEqual(rect_1.x, rect_2.x)
        self.assertEqual(rect_1.y, rect_2.y)
        self.assertEqual(rect_1.id, rect_2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rect_1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Testing Dictionary to JSON string method implemented """
        rect_1 = Rectangle(2, 2)
        dict = rect_1.to_dictionary()
        json_dict = Base.to_json_string([dict])
        res = "[{}]\n".format(dict.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Testing arguments passed """
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Testing arguments passed """
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(1, -2)

    def test_create(self):
        """ Testing create method implemented"""
        dict = {'id': 89}
        rect_1 = Rectangle.create(**dict)
        self.assertEqual(rect_1.id, 89)

    def test_create_2(self):
        """ Testing create method implemented"""
        dict = {'id': 89, 'width': 1}
        rect_1 = Rectangle.create(**dict)
        self.assertEqual(rect_1.id, 89)
        self.assertEqual(rect_1.width, 1)

    def test_create_3(self):
        """ Testing create method implemented"""
        dict = {'id': 89, 'width': 1, 'height': 2}
        rect_1 = Rectangle.create(**dict)
        self.assertEqual(rect_1.id, 89)
        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 2)

    def test_create_4(self):
        """ Testing create method implemented"""
        dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        rect_1 = Rectangle.create(**dict)
        self.assertEqual(rect_1.id, 89)
        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_1.x, 3)

    def test_create_5(self):
        """ Test create method implemented"""
        dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rect_1 = Rectangle.create(**dict)
        self.assertEqual(rect_1.id, 89)
        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_1.x, 3)
        self.assertEqual(rect_1.y, 4)

    def test_load_from_file(self):
        """ Testing the load JSON file method implemented"""
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Testing load JSON file method """
        rect_1 = Rectangle(5, 5)
        rect_2 = Rectangle(8, 2, 5, 5)

        l_input = [rect_1, rect_2]
        Rectangle.save_to_file(l_input)
        l_output = Rectangle.load_from_file()

        for i in range(len(l_input)):
            self.assertEqual(l_input[i].__str__(), l_output[i].__str__())
