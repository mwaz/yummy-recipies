import unittest
from user import Users


class TestUsers(unittest.TestCase):
    """
    class to test the class user
    """
    def setUp(self):
        """ Method called to prepare the test fixture """
        self.newUser = Users()

    def test_member_register(self):
        """ Test to test function member_register """
        self.newUser.users = {}
        #users dictionary to check whether the user already exists
        self.newUser.member_register("waweru@gmail.com", "mwaz", "password", "password")
        result = self.newUser.member_register("waweru@gmail.com", "mwaz", "password", "password")
        self.assertIn("205,Password Regex mismatch", result, "205,Password Regex mismatch")

    def test_null_email_field(self):
        """Test to check if email is null"""
        result = self.newUser.member_register("", "mwaz", "password", "password")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_invalid_member_email(self):
        """Test to ceck emial pattern of member"""
        result = self.newUser.member_register("waweru.waweru.com", "mwaz", "password", "password")
        self.assertIn("205,Email Regex mismatch",result,"205,Email Regex mismatch")

    def test_null_member(self):
        """Test to check if member name is null"""
        result = self.newUser.member_register("waweru@gmail.com", "", "password", "password")
        self.assertIn("205,Regex mismatch", result, "205,Regex mismatch")

    def test_null_password(self):
        """Test to check if email is null"""
        result = self.newUser.member_register("waweru@gmail.com", "mwaz", "", "password")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_null_cpassword(self):
        """ Test to check if cpasword is null """
        result = self.newUser.member_register("waweru@gmail.com", "mwaz", "password", "")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_cpassword_is_equal_to_password(self):
        """Test to check whether the confirm password and the passwords are similar """
        result = self.newUser.member_register("waweru@gmail.com", "mwaz", "password", "pass")
        self.assertIn("400,Passwords dont match", result, "400,Passwords dont match")

    def test_cpassword_is_empty(self):
        """ Test to check whether confirm password field is empty"""
        result = self.newUser.member_register("waweru@gmail.com", "mwaz", "password", " ")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_invalid_member_name(self):
        """Test to check if member_name follows the one specified by regex"""
        member_registration = self.newUser.member_register("waweru@gmail.com", "&#*", "password", "password")
        self.assertIn("205,Regex mismatch", member_registration, "205,Regex mismatch")

    def test_success_login(self):
        """ method to test a successful login """
        self.newUser.users = {}
        self.newUser.member_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('waweru@gmail.com', 'pass')
        self.assertIn("404,User not found", result, "404,User not found")

    def test_wrong_pass_login(self):
        """method to test whether registration password is equal to login password"""
        self.newUser.users = {}
        self.newUser.member_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('waweru@gmail.com', 'pass123')
        self.assertIn("404,User not found", result, "404,User not found")

    def test_wrong_email_login(self):
        """ method to test if the email used for login is wrong"""
        self.newUser.users = {}
        self.newUser.member_register('waweru@gmail.com', 'mwaz', 'pass', 'pass')
        result = self.newUser.user_login('wawerum@gmail.com', 'pass')
        self.assertIn("404,User not found", result, "404,User not found")

    def test_null_email_login(self):
        """ method to test if the email used for login is null"""
        result = self.newUser.user_login('', 'pass')
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_null_login_password(self):
        """ method to test if the password used for login is null """
        result = self.newUser.user_login('waweru@gmail.com', '')
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_null_inputs(self):
        """ method to test if both the password and login is null """
        result = self.newUser.user_login('', '')
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_empty_email(self):
        result = self.newUser.user_login(' ', 'pass')
        self.assertIn("205,Empty input", result, "205,Empty input")

    def test_empty_password(self):
        result = self.newUser.user_login('waweru@gmail.com', ' ')
        self.assertIn("205,Empty input", result, "205,Empty input")
