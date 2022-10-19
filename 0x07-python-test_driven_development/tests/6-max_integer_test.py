#!/usr/bin/python3
'''
Module for testing 6-max_integer.py
'''


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestClass(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, "aba")
    def test_value(self):
        self.assertAlmostEqual(max_integer, )