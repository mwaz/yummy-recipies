import unittest
from unittest import TestCase
from user import Users


class TestUsers(TestCase):
    """
    class to test the class user
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.newUser = Users()

    def test_user_register(self):
        """ Test to test function user_register """
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password","password")
        self.assertEqual(2, res, "User Account Created Successfully")









