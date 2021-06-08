#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.square import Square


class SquareTestCase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):
        s1 = Square(10)
        s2 = Square(2, 0, 1)
        s3 = Square(10, 2, 12)
        s4 = Square(1, 1, 1, 55)
        s5 = Square(2, 0, 0, -23)
        s6 = Square(1, 1, 1, [123, 456])
        s7 = Square(30, 1, 0, {1, 2, 3})
        s8 = Square(10, 0, 0, "12")
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s2.id, s3.id - 1)
        self.assertEqual(s3.id, s2.id + 1)
        self.assertEqual(s4.id, 55)
        self.assertEqual(s5.id, -23)
        self.assertEqual(s6.id, [123, 456])
        self.assertEqual(s7.id, {1, 2, 3})
        self.assertEqual(s8.id, "12")

        with self.assertRaises(TypeError):
            Square()
            Square('2')
            Square(1, 1, 1, 1, 1, 1, 1)
            Square([])
            Square({})
            Square(10, "2", "0", "12")
            Square(float('inf'))

        with self.assertRaises(ValueError):
            Square(0)
            Square(-1)
            Square(1, 0, -1)
            Square(3, -3, 9)

    def test_square_str(self):
        s = Square(3, 0, 0, 100)

        with redirect_stdout(io.StringIO()) as f:
            print(s)
        self.assertEqual("[Square] (100) 0/0 - 3\n", f.getvalue())

        s = Square(2, 1, 80, "[1]134,")

        with redirect_stdout(io.StringIO()) as f:
            print(s)
        self.assertEqual("[Square] ([1]134,) 1/80 - 2\n", f.getvalue())

        s = Square(13, 9, 9, [2, 2, 2])

        with redirect_stdout(io.StringIO()) as f:
            print(s)
        self.assertEqual("[Square] ([2, 2, 2]) 9/9 - 13\n", f.getvalue())

    def test_square_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        s.size = 22
        self.assertEqual(s.size, 22)

        with self.assertRaises(TypeError):
            s.size = "11"
            s.size = [2, 3, 4, 5]
            s.size = {2: 3, 4: 5}
            s.size = (2, 3, 4, 5)
            s.size = 2.342,
            s.size = None,
            s.size = float('inf')
            s.size = float('nan')

        with self.assertRaises(ValueError):
            s.size = -2
            s.size = 0

    def test_square_update(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(89, 2, 4, 5)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
        s.update(129, 1, 1, 1, 1)
        self.assertEqual(s.id, 129)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        s.update(size=21)
        self.assertEqual(s.size, 21)
        s.update(size=1, x=2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.id, 89)
        s.update(x=1, size=32, y=3, id=4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.size, 32)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        s.update(noattr=9)
        self.assertEqual(hasattr(s, "noattr"), False)
        s.update(id={})
        self.assertEqual(s.id, {})
        s.update(129, 1, 1, size=2, x=2)
        self.assertEqual(s.id, 129)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 1)

        with self.assertRaises(ValueError):
            s.update(33, 0)
            s.update(129, 0, 3, 5)
            s.update(9, 2, -1, 4)
            s.update(4, 10, 12, -1)
            s.update(90, -16, 18, 1)
            s.update(y=1, size=0)
            s.update(y=-1, x=0)
            s.update(id=1, size=0)
            s.update(size=0)

        with self.assertRaises(TypeError):
            s.update(129, [], 3, 5)
            s.update(129, 1, 3, {})
            s.update(129, 1, 3.43, 7)
            s.update(129, 1, b'ocho', 7)
            s.update(y=1, size=[])
            s.update(y=b'bytes', x=0)
            s.update(id=1, size=89.0987)
            s.update(size=float('inf'))

    def test_square_to_dictionary(self):
        s1 = Square(2, 1, 9)
        s_dict = s1.to_dictionary()
        answer = {'x': 1, 'y': 9, 'id': 1, 'size': 2}
        self.assertDictEqual(s_dict, answer)

        s = Square(1)
        s.update(**s_dict)
        self.assertDictEqual(s.to_dictionary(), answer)
        self.assertNotEqual(s1, s)

        s = Square(6)
        answer = {'x': 0, 'y': 0, 'id': 3, 'size': 6}
        self.assertDictEqual(s.to_dictionary(), answer)

        s = Square(1, 1, 1, -56)
        answer = {'x': 1, 'y': 1, 'id': -56, 'size': 1}
        self.assertDictEqual(s.to_dictionary(), answer)

if __name__ == "__main__":
    unittest.main()
