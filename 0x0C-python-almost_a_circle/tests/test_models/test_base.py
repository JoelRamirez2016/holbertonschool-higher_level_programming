#!/usr/bin/python3
"""Unittest for base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        """No need to test type in id attr"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base(5)
        b6 = Base(5)
        b7 = Base("123")
        b8 = Base([1, 2, 3])
        b9 = Base({1: 1, 2: 2})
        b10 = Base({1, 2, 3})
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b3.id, b4.id - 1)
        self.assertEqual(b4.id, b3.id + 1)
        self.assertEqual(b5.id, 5)
        self.assertEqual(b6.id, 5)
        self.assertEqual(b7.id, "123")
        self.assertEqual(b8.id, [1, 2, 3])
        self.assertEqual(b9.id, {1: 1, 2: 2})

    def test_base_to_json_string(self):
        """Args of to_json_string is always list of dicts"""
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        l = [{'id': 23}, {'id': -23}, {'id': 45}, {'id': {'id': []}}]
        ans = '[{"id": 23}, {"id": -23}, {"id": 45}, {"id": {"id": []}}]'
        self.assertEqual(Base.to_json_string(l), ans)
        l = [{'x': 2, 'width': 1, 'id': 41, 'height': 57, 'y': 1},
             {'x': 12, 'width': 210, 'id': 31, 'height': 57, 'y': 0},
             {'x': 23, 'width': 40, 'id': 11, 'height': 8, "y": 5}]
        self.assertEqual(len(Base.to_json_string(l)), 166)
        l = [{'x': 2, 'size': 1, 'id': 41, 'y': 1},
             {'x': 12, 'size': 210, 'id': 31, 'y': 0},
             {'x': 23, 'size': 40, 'id': 11, 'y': 5}]
        self.assertEqual(len(Base.to_json_string(l)), 122)

        r1 = Rectangle(2, 1)
        s1 = Square(3)
        s2 = Square(2)
        self.assertEqual(len(Rectangle.to_json_string(
                             [r1.to_dictionary()])), 52)
        self.assertEqual(len(Square.to_json_string([s1.to_dictionary(),
                                                    s2.to_dictionary()])), 76)
        self.assertEqual(len(Base.to_json_string([r1.to_dictionary(),
                                                  s1.to_dictionary(),
                                                  s2.to_dictionary()])), 128)

        with self.assertRaises(TypeError):
            Base.to_json_string()
            Base.to_json_string(1, 1, 1)
            Base.to_json_string(b)
            Base.to_json_string(r1)
            Base.to_json_string(s1)

    def test_base_save_to_file(self):
        b1 = Base()
        b2 = Base(2)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(2)
        s2 = Square(3)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 105)

        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 76)

        Base.save_to_file([r1, r2, s1, s2])
        with open("Base.json", "r") as f:
            self.assertEqual(len(f.read()), 181)

        Rectangle.save_to_file([s1, s2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 76)

        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 105)

        with self.assertRaises(AttributeError):
            Base.save_to_file([b1, b2])

        os.remove("Rectangle.json")
        os.remove("Square.json")
        os.remove("Base.json")

    def test_base_from_json_string(self):
        li = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json = Rectangle.to_json_string(li)
        self.assertEqual(Rectangle.from_json_string(json), li)
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

        json = '[{"id": 23}, {"id": -23}, {"id": 45}, {"id": {"id": []}}]'
        li = [{'id': 23}, {'id': -23}, {'id': 45}, {'id': {'id': []}}]
        self.assertEqual(Base.from_json_string(json), li)

        li = [{'x': 2, 'width': 1, 'id': 41, 'height': 57, 'y': 1},
              {'x': 12, 'width': 210, 'id': 31, 'height': 57, 'y': 0},
              {'x': 23, 'width': 40, 'id': 11, 'height': 8, "y": 5}]
        json = Base.to_json_string(li)
        self.assertEqual(Base.from_json_string(json), li)

        li = [{'x': 2, 'size': 1, 'id': 41, 'y': 1},
              {'x': 12, 'size': 210, 'id': 31, 'y': 0},
              {'x': 23, 'size': 40, 'id': 11, 'y': 5}]
        json = Base.to_json_string(li)
        self.assertEqual(Base.from_json_string(json), li)

        r1 = Rectangle(2, 1)
        s1 = Square(3)
        s2 = Square(2)
        li = [r1.to_dictionary()]
        json = Rectangle.to_json_string(li)
        self.assertEqual(Rectangle.from_json_string(json), li)

        li = [s1.to_dictionary(), s2.to_dictionary()]
        json = Square.to_json_string(li)
        self.assertEqual(Square.from_json_string(json), li)

        li = [r1.to_dictionary(), s1.to_dictionary(), s2.to_dictionary()]
        json = Base.to_json_string(li)
        self.assertEqual(Base.from_json_string(json), li)

        with self.assertRaises(TypeError):
            Base.from_json_string()
            Base.from_json_string(1, 1, 1)

    def test_base_create(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        s1 = Square(3, 5, 1)
        s2 = Square.create(**s1.to_dictionary())
        r3 = Rectangle(3, 1, 0, 0, 8)
        r4 = Rectangle.create(id=8, width=3)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)
        self.assertDictEqual(r3.to_dictionary(), r4.to_dictionary())

        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_base_load_from_file(self):
        l = Rectangle.load_from_file()
        self.assertEqual(l, [])

        l = Square.load_from_file()
        self.assertEqual(l, [])

        r1 = Rectangle(3, 1)
        r2 = Rectangle(1, 2)
        Rectangle.save_to_file([r1, r2])
        list_objects = Rectangle.load_from_file()
        self.assertTrue(all(o.id in [r1.id, r2.id] for o in list_objects))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        list_objects = Square.load_from_file()
        self.assertTrue(all(o.id in [s1.id, s2.id] for o in list_objects))

        Rectangle.save_to_file([s1, r1, s2, r2])
        l = Rectangle.load_from_file()
        self.assertTrue(all(o.id in [s1.id, r1.id, s2.id, r2.id] for o in l))

        with self.assertRaises(TypeError):
            Base.load_from_file("no needed")

        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_base_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(5)
        s2 = Square(9)
        s3 = Square(10, 7, 2, 8)

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(len(f.read()), 0)

        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            csvExpected = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
            self.assertEqual(csvExpected, f.read())

        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            csvExpected = "id,size,x,y\n3,5,0,0\n4,9,0,0\n"
            self.assertEqual(csvExpected, f.read())

        Base.save_to_file_csv([s3])
        with open("Base.csv", "r") as f:
            csvExpected = "id,size,x,y\n8,10,7,2\n"
            self.assertEqual(csvExpected, f.read())

        Square.save_to_file_csv({s1, s2})
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()
            Rectangle.save_to_file_csv()
            Square.save_to_file_csv("NO NEEDED")

        with self.assertRaises(AttributeError):
            Square.save_to_file_csv({2, 3, 4})
            Base.save_to_file_csv([r2])

        os.remove("Rectangle.csv")
        os.remove("Square.csv")
        os.remove("Base.csv")

    def test_base_load_from_file_csv(self):
        l = Rectangle.load_from_file_csv()
        self.assertEqual(l, [])

        l = Square.load_from_file_csv()
        self.assertEqual(l, [])

        r1 = Rectangle(3, 1)
        r2 = Rectangle(1, 2)
        Rectangle.save_to_file_csv([r1, r2])
        l = Rectangle.load_from_file_csv()
        self.assertTrue(all(o.id in [r1.id, r2.id] for o in l))

        s1 = Square(25)
        s2 = Square(20, 2, 3, 56)
        Square.save_to_file_csv([s1])
        l = Square.load_from_file_csv()
        self.assertTrue(all(o.id in [s1.id] for o in l))

        Base.save_to_file_csv([s1, s2])
        with self.assertRaises(AttributeError):
            Base.load_from_file_csv()

        os.remove("Rectangle.csv")
        os.remove("Square.csv")
        os.remove("Base.csv")
