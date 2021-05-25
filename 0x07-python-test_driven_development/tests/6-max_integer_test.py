#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([11, 25, 8]), 25)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer("12345678"), '8')
        self.assertEqual(max_integer((1, 2, 3, 4, 5, 6, 7, 8, 9, 44)), 44)
        self.assertEqual(max_integer("abcdefghijklmnopqrs"), 's')
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
