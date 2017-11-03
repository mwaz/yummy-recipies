import unittest

from models.user import Users
from app import app


class TestUsers(unittest.TestCase):
    """
    class to test the class user
    """

    def setUp(self):
        """ Method called to prepare the test fixture """
        self.newUser = Users()
        self.register = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "password", "password")
        app.config['TESTING'] = True
        self.test_app = app.test_client()

    def test_user_email_exists_on_register(self):
        """ Test to if user email exists on register """
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaze", "password", "password")
        self.assertEqual("Email exists", result)

    def test_user_register_success(self):
        """ Test to test function user_register """
        result = self.newUser.user_register(
            "waweruhm@gmail.com", "mwazz", "password6", "password6")
        self.assertEqual("Successfully created account", result)

    def test_null_email_field(self):
        """Test to check if email is null"""
        result = self.newUser.user_register("", "mwaz", "password", "password")
        self.assertEqual("please input all fields", result)

    def test_invalid_user_email(self):
        """Test to ceck emial pattern of member"""
        result = self.newUser.user_register(
            "waweru.waweru.com", "mwaz", "password", "password")
        self.assertEqual("Email format is invalid", result)

    def test_null_username(self):
        """Test to check if user name is null"""
        result = self.newUser.user_register(
            "waweru@gmail.com", "", "password", "password")
        self.assertEqual("please input all fields", result)

    def test_null_password(self):
        """Test to check if email is null"""
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "", "password")
        self.assertEqual("please input all fields", result)

    def test_null_cpassword(self):
        """ Test to check if cpasword is null """
        result = self.newUser.user_register(
            "waweru@gmail.com", "mwaz", "password", "")
        self.assertEqual("please input all fields", result)

    def test_password_length(self):
        """ Test to check the length of password """
        result = self.newUser.user_register(
            "waweruh@gmail.com", "mwaz", "passwo", "passwo")
        self.assertEqual(
            "password length should be atleast 8 characters", result)

    def test_root_route(self):
        """ test to see that homepage loads"""
        response = self.test_app.get('/')
        self.assertIn(b'Index', response.data)

    def test_cpassword_is_equal_to_password(self):
        """Test to check whether the confirm password and the passwords are similar """
        result = self.newUser.user_register(
            "wawerum@gmail.com", "mwaz2", "password", "pass")
        self.assertEqual("Passwords dont match", result)

    def test_invalid_user_name(self):
        """Test to check if member_name follows the one specified by regex"""
        member_registration = self.newUser.user_register(
            "waweru@gmail.com", "&#*", "password", "password")
        self.assertEqual("username should not have special characters or spaces",
                         member_registration)

    def test_wrong_pass_login(self):
        """method to test whether registration password is equal to login password"""

        result = self.newUser.user_login('waweru@gmail.com', 'pass123')
        self.assertEqual("Password mismatch", result)

    def test_wrong_email_login(self):
        """ method to test if the email used for login is wrong"""
        self.register
        result = self.newUser.user_login('wawerum@gmail.com', 'pass')
        self.assertEqual("email not found", result)

    def test_null_email_login(self):
        """ method to test if the email used for login is null"""
        result = self.newUser.user_login('', 'pass')
        self.assertEqual("empty email or password fields", result)

    def test_null_login_password(self):
        """ method to test if the password used for login is null """
        result = self.newUser.user_login('waweru@gmail.com', '')
        self.assertEqual("empty email or password fields", result)

    def test_null_inputs(self):
        """ method to test if both the password and login is null """
        result = self.newUser.user_login('', '')
        self.assertEqual("empty email or password fields", result)
