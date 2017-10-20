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
        self.newUser.users = {} #users dictionary to check whether the user already exists
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

    def test_success_login(self):
        """ method to test a successful login """
        self.newUser.users = {}
        self.newUser.user_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('waweru@gmail.com', 'pass')
        self.assertEqual(3, result, "Successful login")

    def test_wrong_pass_login(self):
        """method to test whether registration password is equal to login password"""
        self.newUser.users = {}
        self.newUser.user_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('waweru@gmail.com', 'pass123')
        self.assertEqual(3, result, "Wrong login credentials")

    def test_wrong_email_login(self):
        """ method to test if the email used for login is wrong"""
        self.newUser.users = {}
        self.newUser.user_register('waweru@gmail.com', 'mwaz', 'pass','pass')
        result = self.newUser.user_login('wawerum@gmail.com', 'pass')
        self.assertEqual(3, result, "wrong login credentials")

    def test_null_email_login(self):
        """ method to test if the email used for login is null"""
        result = self.newUser.user_login('','pass')
        self.assertEqual(4,result, "Kindly fill the email field")

    def test_null_password(self):
        """ method to test if the password used for login is null """
        result = self.newUser.user_login('waweru@gmail.com', '')
        self.assertEqual(4, result, "Kindly fill the password field")

    def test_null_inputs(self):
        """ method to test if both the password and login is null """
        result = self.newUser.user_login('', '')
        self.assertEqual(4, result, "Kindly fill in all fields")

    def test_empty_email(self):
        result = self.newUser.user_login(' ', 'pass')
        self.assertEqual(5, result, "Email field is empty")

    def test_empty_password(self):
        result = self.newUser.user_login('waweru@gmail.com', ' ')
        self.assertEqual(5, result,"Password filed is empty")
