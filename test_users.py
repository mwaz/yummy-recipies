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

    def test_null_email(self):
        """Test to check if email is null"""
        res = self.newUser.user_register(" ", "mwaz", "password", "password")
        self.assertEqual(7, res, "Please provide an email address")

    def test_null_username(self):
        """Test to check if username is null"""
        res = self.newUser.user_register("waweru@gmail.com", " ", "password", "password")
        self.assertEqual(7, res, "Please provide a username")

    def test_null_password(self):
        """Test to check if email is null"""
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", " ", "password")
        self.assertEqual(7, res, "No password provided")

    def test_cpassword_is_equal_to_password(self):
        """Test to check whether the confirm password and the passwords are similar """
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password", "pass")
        self.assertEqual(4, res, "The passwords do not match")











