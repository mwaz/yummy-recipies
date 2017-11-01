import unittest

from models.user import Users


class TestUsers(unittest.TestCase):
    """
    class to test the class user
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.newUser = Users()
        self.register = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "password", "password")

    def test_user_email_exists_on_register(self):
        """ Test to if user email exists on register """
        self.register
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaze", "password", "password")
        self.assertIn("401,Email exists", result, "401,Email exists")

    def test_user_register_success(self):
        """ Test to test function user_register """
        result = self.newUser.user_register(
            "waweruhm@gmail.com", "mwazz", "password6", "password6")
        self.assertIn("200,OK", result, "200,OK")

    def test_null_email_field(self):
        """Test to check if email is null"""
        result = self.newUser.user_register("", "mwaz", "password", "password")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_invalid_member_email(self):
        """Test to ceck emial pattern of member"""
        result = self.newUser.user_register(
            "waweru.waweru.com", "mwaz", "password", "password")
        self.assertIn("205,Email Regex mismatch",
                      result, "205,Email Regex mismatch")

    def test_null_member(self):
        """Test to check if user name is null"""
        result = self.newUser.user_register(
            "waweru@gmail.com", "", "password", "password")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_null_password(self):
        """Test to check if email is null"""
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "", "password")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_null_cpassword(self):
        """ Test to check if cpasword is null """
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "password", "")
        self.assertIn("205,Invalid input", result, "205,Invalid input")

    def test_cpassword_is_equal_to_password(self):
        """Test to check whether the confirm password and the passwords are similar """
        result = self.newUser.user_register(
            "wawerum@gmail.com", "mwaz2", "password", "pass")
        self.assertIn("400,Passwords dont match",
                      result, "400,Passwords dont match")

    def test_invalid_member_name(self):
        """Test to check if member_name follows the one specified by regex"""
        member_registration = self.newUser.user_register(
            "waweru@gmail.com", "&#*", "password", "password")
        self.assertIn("205,Regex mismatch",
                      member_registration, "205,Regex mismatch")

    def test_existing_member_email(self):
        """ Test to check if email exists"""
        self.register
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "password2", "password2")
        self.assertIn("401,Email exists", result, "401,Email exists")

    def test_invalid_login_credentials(self):
        """ method to test a successful login """
        self.register
        result = self.newUser.user_login('waweruh@gmail.com', 'ppass')
        self.assertIn("404,User not found", result, "404,User not found")

    def test_wrong_pass_login(self):
        """method to test whether registration password is equal to login password"""
        self.register
        result = self.newUser.user_login('waweru@gmail.com', 'pass123')
        self.assertIn("205,Password mismatch", result, "205,Password mismatch")

    def test_wrong_email_login(self):
        """ method to test if the email used for login is wrong"""
        self.register
        result = self.newUser.user_login('wawerum@gmail.com', 'pass')
        self.assertIn("404,User not found", result, "404,User not found")

    def test_null_email_login(self):
        """ method to test if the email used for login is null"""
        result = self.newUser.user_login('', 'pass')
        self.assertIn("205,Empty input", result, "205,Empty input")

    def test_null_login_password(self):
        """ method to test if the password used for login is null """
        result = self.newUser.user_login('waweru@gmail.com', '')
        self.assertIn("205,Empty input", result, "205,Empty input")

    def test_null_inputs(self):
        """ method to test if both the password and login is null """
        result = self.newUser.user_login('', '')
        self.assertIn("205,Empty input", result, "205,Empty input")

    def test_member_email_fetch(self):
        """Test to check if get_email method returns the correct email"""
        email = "mwaz@gmail.com"
        result = self.newUser.get_registered_user_email(email)
        self.assertEqual(result, email)
