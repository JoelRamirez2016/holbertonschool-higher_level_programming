#!/usr/bin/python3
"""Unittest for base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_init(self):
        """No need to test type"""
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
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 5)
        self.assertEqual(b6.id, 5)
        self.assertEqual(b7.id, "123")
        self.assertEqual(b8.id, [1, 2, 3])
        self.assertEqual(b9.id, {1: 1, 2: 2})
        self.assertEqual(b10.id, {1, 2, 3})
