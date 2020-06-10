#!/usr/bin/env python

import unittest

from validate_user import validate_username

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_username("testts", 1), True)
    def test_invalid(self):
        self.assertEqual(validate_username("tes", 5), False)
    def test_value(self):
        self.assertRaises(ValueError, validate_username, "username", -1)

unittest.main()
