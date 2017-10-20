import unittest
from unittest import TestCase
from user import Users


class TestUsers(unittest.TestCase):
    """
    class to test the class user
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.newUser = Users()

    def test_user_register(self):
        """ Test to test function user_register """
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password", "password")
        self.assertEqual(2, res, "User Account Created Successfully")

    def test_null_email_field(self):
        """Test to check if email is null"""
        res = self.newUser.user_register("", "mwaz", "password", "password")
        self.assertEqual(7, res, "Please provide an email address")

    def test_null_username(self):
        """Test to check if username is null"""
        res = self.newUser.user_register("waweru@gmail.com", "", "password", "password")
        self.assertEqual(8, res, "Please provide a username")

    def test_null_password(self):
        """Test to check if email is null"""
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "", "password")
        self.assertEqual(7, res, "No password provided")

    def test_null_cpassword(self):
        """ Test to check if cpasword is null """
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password", "")
        self.assertEqual(7, res, "Confirm Password not provided ")

    def test_cpassword_is_equal_to_password(self):
        """Test to check whether the confirm password and the passwords are similar """
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password", "pass")
        self.assertEqual(4, res, "Invalid credentials, kindly try again")

    def test_cpassword_is_empty(self):
        """ Test to check whether confirm password field is empty"""
        res = self.newUser.user_register("waweru@gmail.com", "mwaz", "password", " ")
        self.assertEqual(7, res, "Confirm Password field is empty")

    def test_pass_in_login(self):
        """method to test whether registration password is equal to login password"""
        self.newUser.users = {}
        self.newUser.user_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('waweru@gmail.com', 'pass123')
        self.assertEqual(3, result, "Wrong login credentials")

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.users = {}
        self.newUser.register('muthomi@gmail.com', 'muthomi', 'pass','pass')
        result = self.newUser.login('muthomimate@gmail.com', 'pass')
        self.assertEqual(3, result, "wrong login credentials")
