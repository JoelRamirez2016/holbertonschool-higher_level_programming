#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(10, 2)

    def test_rectangle(self):
        r1 = self.r
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(1, 1, 0, 0, "123")
        r5 = Rectangle(1, 1, 0, 0, [1, 2, 3])
        r6 = Rectangle(10, 3, 0, 2, {1: 1, 2: 2})
        r7 = Rectangle(30, 1, 0 ,0 ,{1, 2, 3})
        r8 = Rectangle(10, 2, 0, 0, "12")
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, "123")
        self.assertEqual(r5.id, [1, 2, 3])
        self.assertEqual(r6.id, {1: 1, 2: 2})
        self.assertEqual(r7.id, {1, 2, 3})
        self.assertEqual(r8.id, "12")

        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(2)
            Rectangle(2, 2, '3', 1)
            Rectangle(2, 2, 3, '1')
            Rectangle(10, "2", "0", "0", "12")
            Rectangle([2, 2, 2, 2], {1, 2, 3}, 0, 0, 12)

    def test_rectangle_width(self):
        self.assertEqual(self.r.width, 10)
        self.r.width = 22
        self.assertEqual(self.r.width, 22)

        with self.assertRaises(TypeError):
            self.r.width = "11"
            self.r.width = [2, 3, 4, 5]
            self.r.width = {2: 3, 4: 5}
            self.r.width = (2, 3, 4, 5)
            self.r.width = 2.342,
            self.r.width = None,
            self.r.width = float('inf')
            self.r.width = float('nan')

        with self.assertRaises(ValueError):
            self.r.width = -2
            self.r.width = 0

    def test_rectangle_height(self):
        self.assertEqual(self.r.height, 2)
        self.r.height = 22
        self.assertEqual(self.r.height, 22)

        with self.assertRaises(TypeError):
            self.r.height = "11"
            self.r.height = [2, 3, 4, 5]
            self.r.height = {2: 3, 4: 5}
            self.r.height = (2, 3, 4, 5)
            self.r.height = 2.342,
            self.r.height = None,
            self.r.height = float('inf')
            self.r.height = float('nan')

        with self.assertRaises(ValueError):
            self.r.height = -2
            self.r.height = 0

    def test_rectangle_x(self):
        self.assertEqual(self.r.x, 0)
        self.r.x = 1
        self.assertEqual(self.r.x, 1)
        self.r.x = 0
        self.assertEqual(self.r.x, 0)

        with self.assertRaises(TypeError):
            self.r.x = "11"
            self.r.x = [2, 3, 4, 5]
            self.r.x = {2: 3, 4: 5}
            self.r.x = (2, 3, 4, 5)
            self.r.x = 2.342,
            self.r.x = None,
            self.r.x = float('inf')
            self.r.x = float('nan')

        with self.assertRaises(ValueError):
            self.r.x = -2

    def test_rectangle_y(self):
        self.assertEqual(self.r.y, 0)
        self.r.y = 1
        self.assertEqual(self.r.y, 1)
        self.r.y = 0
        self.assertEqual(self.r.y, 0)

        with self.assertRaises(TypeError):
            self.r.y = "11"
            self.r.y = [2, 3, 4, 5]
            self.r.y = {2: 3, 4: 5}
            self.r.y = (2, 3, 4, 5)
            self.r.y = 2.342,
            self.r.y = None,
            self.r.y = float('inf')
            self.r.y = float('nan')

        with self.assertRaises(ValueError):
            self.r.y = -2


    def test_rectangle_area(self):
        r1 = Rectangle(2, 5)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(1, 1, 0, 0, "123")
        r5 = Rectangle(1, 1, 0, 0, [1, 2, 3])
        r6 = Rectangle(10, 3, 0, 2, {1: 1, 2: 2})
        r7 = Rectangle(30, 1, 0 ,0 ,{1, 2, 3})

        self.assertEqual(r1.area(), 10)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r3.area(), 20)
        self.assertEqual(r4.area(), 1)
        self.assertEqual(r5.area(), 1)
        self.assertEqual(r6.area(), 30)
        self.assertEqual(r7.area(), 30)

    def test_rectangle_display(self):
        self.r.width = 1
        self.r.height = 1

        with redirect_stdout(io.StringIO()) as f:
            self.r.display()
        self.assertEqual("#\n", f.getvalue())

        self.r.height = 2
        with redirect_stdout(io.StringIO()) as f:
            self.r.display()
        self.assertEqual("#\n#\n", f.getvalue())

        self.r.width = 5
        with redirect_stdout(io.StringIO()) as f:
            self.r.display()
        self.assertEqual("#####\n#####\n", f.getvalue())

        self.r.height = 5
        with redirect_stdout(io.StringIO()) as f:
            self.r.display()
        self.assertEqual("#####\n#####\n#####\n#####\n#####\n", f.getvalue())
