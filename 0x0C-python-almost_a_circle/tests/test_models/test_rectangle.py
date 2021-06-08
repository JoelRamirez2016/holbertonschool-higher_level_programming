#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(1, 1, 0, 0, "123")
        r5 = Rectangle(1, 1, 0, 0, [1, 2, 3])
        r6 = Rectangle(10, 3, 0, 2, {1: 1, 2: 2})
        r7 = Rectangle(30, 1, 0, 0, {1, 2, 3})
        r8 = Rectangle(10, 2, 0, 0, "12")
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r1.id + 1)
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
            Rectangle(2, 0, 0, 1)
            Rectangle(2, 2, 3, '1')
            Rectangle(10, "2", "0", "0", "12")
            Rectangle([2, 2, 2, 2], {1, 2, 3}, 0, 0, 12)
            Rectangle(3.3, 4)
            Rectangle(2, float('inf'))
            Rectangle(1, float('nan'))
            Rectangle(45, False)
            Rectangle(complex(3), 3, 3)
            Rectangle(2, b'bId')

    def test_rectangle_width(self):
        r = Rectangle(10, 1)
        self.assertEqual(r.width, 10)
        r.width = 22
        self.assertEqual(r.width, 22)

        with self.assertRaises(TypeError):
            r.width = "11"
            r.width = [2, 3, 4, 5]
            r.width = {2: 3, 4: 5}
            r.width = (2, 3, 4, 5)
            r.width = 2.342,
            r.width = None,
            r.width = float('inf')
            r.width = float('nan')

        with self.assertRaises(ValueError):
            r.width = -2
            r.width = 0

    def test_rectangle_height(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)
        r.height = 22
        self.assertEqual(r.height, 22)

        with self.assertRaises(TypeError):
            r.height = "11"
            r.height = [2, 3, 4, 5]
            r.height = {2: 3, 4: 5}
            r.height = (2, 3, 4, 5)
            r.height = 2.342,
            r.height = None,
            r.height = float('inf')
            r.height = float('nan')

        with self.assertRaises(ValueError):
            r.height = -2
            r.height = 0

    def test_rectangle_x(self):
        r = Rectangle(10, 3)
        self.assertEqual(r.x, 0)
        r.x = 1
        self.assertEqual(r.x, 1)
        r.x = 0
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError):
            r.x = "11"
            r.x = [2, 3, 4, 5]
            r.x = {2: 3, 4: 5}
            r.x = (2, 3, 4, 5)
            r.x = 2.342,
            r.x = None,
            r.x = float('inf')
            r.x = float('nan')

        with self.assertRaises(ValueError):
            r.x = -2

    def test_rectangle_y(self):
        r = Rectangle(2, 2)
        self.assertEqual(r.y, 0)
        r.y = 1
        self.assertEqual(r.y, 1)
        r.y = 0
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r.y = "11"
            r.y = [2, 3, 4, 5]
            r.y = {2: 3, 4: 5}
            r.y = (2, 3, 4, 5)
            r.y = 2.342,
            r.y = None,
            r.y = float('inf')
            r.y = float('nan')

        with self.assertRaises(ValueError):
            r.y = -2

    def test_rectangle_area(self):
        r1 = Rectangle(2, 5)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(1, 1, 0, 0, "123")
        r5 = Rectangle(1, 1, 0, 0, [1, 2, 3])
        r6 = Rectangle(10, 3, 0, 2, {1: 1, 2: 2})
        r7 = Rectangle(30, 1, 0, 0, {1, 2, 3})

        self.assertEqual(r1.area(), 10)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r3.area(), 20)
        self.assertEqual(r4.area(), 1)
        self.assertEqual(r5.area(), 1)
        self.assertEqual(r6.area(), 30)
        self.assertEqual(r7.area(), 30)

    def test_rectangle_display(self):
        r = Rectangle(1, 1)

        with redirect_stdout(io.StringIO()) as f:
            r.display()
        self.assertEqual("#\n", f.getvalue())

        r.height = 2
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        self.assertEqual("#\n#\n", f.getvalue())

        r.width = 5
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        self.assertEqual("#####\n#####\n", f.getvalue())

        r.height = 5
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        self.assertEqual("#####\n#####\n#####\n#####\n#####\n", f.getvalue())

        r = Rectangle(5, 2, 3, 3)
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        answer = ("\n\n\n" +
                  "   #####\n" +
                  "   #####\n")
        self.assertEqual(answer, f.getvalue())

        r.width = 2
        r.y = 0
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        answer = ("   ##\n" +
                  "   ##\n")
        self.assertEqual(answer, f.getvalue())

        r.height = 4
        r.y = 1
        with redirect_stdout(io.StringIO()) as f:
            r.display()
        answer = ("\n" +
                  "   ##\n" +
                  "   ##\n" +
                  "   ##\n" +
                  "   ##\n")
        self.assertEqual(answer, f.getvalue())

    def test_rectangle_str(self):
        r = Rectangle(3, 3, 0, 0, 100)

        with redirect_stdout(io.StringIO()) as f:
            print(r)
        self.assertEqual("[Rectangle] (100) 0/0 - 3/3\n", f.getvalue())

        r = Rectangle(3, 2, 1, 80, "[1]134,")

        with redirect_stdout(io.StringIO()) as f:
            print(r)
        self.assertEqual("[Rectangle] ([1]134,) 1/80 - 3/2\n", f.getvalue())

        r = Rectangle(13, 9, 9, 9, [2, 2, 2])

        with redirect_stdout(io.StringIO()) as f:
            print(r)
        self.assertEqual("[Rectangle] ([2, 2, 2]) 9/9 - 13/9\n", f.getvalue())

    def test_rectangle_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(129, 1, 1, 1, 1)
        self.assertEqual(r.id, 129)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        r.update(height=1)
        self.assertEqual(r.height, 1)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.y, 3)
        r.update(noattr=9)
        r.update(id={})
        self.assertEqual(r.id, {})
        r.update(129, 1, 1, width=2, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)

        with self.assertRaises(ValueError):
            r.update(129, 0, 3, 5, 7)
            r.update(9, 2, -1, 4, 8)
            r.update(4, 10, 12, -1, 14)
            r.update(90, 16, 18, 20, -1)
            r.update(y=1, width=0)
            r.update(y=-1, x=0)
            r.update(id=1, width=0)
            r.update(height=-1, width=0)

        with self.assertRaises(TypeError):
            r.update(129, [], 3, 5, 7)
            r.update(129, 1, 3, 5, {})
            r.update(129, 1, 3.43, 8, 7)
            r.update(129, 1, 3, b'ocho', 7)
            r.update(y=1, width=[])
            r.update(y=b'bytes', x=0)
            r.update(id=1, width=89.0987)
            r.update(height=float('inf'), width=0)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r_dict = r1.to_dictionary()
        answer = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r_dict, answer)

        r = Rectangle(1, 1)
        r.update(**r_dict)
        self.assertDictEqual(r.to_dictionary(), answer)
        self.assertNotEqual(r1, r)

        r = Rectangle(5, 6)
        answer = {'x': 0, 'y': 0, 'id': 3, 'height': 6, 'width': 5}
        self.assertDictEqual(r.to_dictionary(), answer)

        r = Rectangle(1, 1, 1, 1, -56)
        answer = {'x': 1, 'y': 1, 'id': -56, 'height': 1, 'width': 1}
        self.assertDictEqual(r.to_dictionary(), answer)

if __name__ == "__main__":
    unittest.main()
