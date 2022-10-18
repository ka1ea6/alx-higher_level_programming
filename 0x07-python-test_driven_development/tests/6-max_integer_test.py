#!/usr/bin/python3
'''
Module for testing 6-max_integer.py
'''


import unittest

class TestClass(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, "aba")