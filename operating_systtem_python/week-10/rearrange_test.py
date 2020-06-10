#!/usr/bin/env python

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        test_case = "Lovely,Ida"
        expected = "Ida Lovely"
        self.assertEqual(rearrange_name(test_case), expected)
    def test_empty(self):
        test_case = ""
        expected = ""
        self.assertEqual(rearrange_name(test_case), expected)
    def test_double_name(self):
        test_case = "Das,Bhabani. Sankar"
        expected = "Bhabani. Sankar Das"
        self.assertEqual(rearrange_name(test_case), expected)
    def test_one_name(self):
        test_case = "Das"
        expected = "Das"
        self.assertEqual(rearrange_name(test_case), expected)
unittest.main()
