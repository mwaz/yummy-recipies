"""Class that defines how to create a user and log them in"""
import re


class Users(object):
    """
    Users Class to handle  user functions like login and signup
    """
    # Dictionary to store the user details
    # storing a default user for testing purposes, avoiding signup on
    # every server restart

    def __init__(self, username=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.regex_username = "[a-zA-Z0-9- .]+$"
        self.users = {}
        self.regex_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        self.regex_name = "[a-zA-Z0-9- .]+$"
        self.users = {'mwaz@gmail.com': {'username': 'mwaz',
                                         'email': 'mwaz@gmail.com',
                                         'password': '1234567q'}}

    def user_register(self, email, username, password, cpassasword):
        """
         method that defines the how to to create a user account
         sample structure of how data is stored:
         users = { email : { 'username': username,
                             'email',: email,
                             'password',: password}}
        The email is the key to every user and is unique
        """

        if username:
            username = re.sub(r'\s+', ' ', username).strip()
        username = None if username == " " else username

        if email:
            lowercase_email = email.lower()
        email = lowercase_email

        if not (username and email and password and cpassasword):
            return "please input all fields"

        if not re.search(self.regex_username, username):
            return "username should not have special characters or spaces"

        if not re.search(self.regex_email, email):
            return "Email format is invalid"

        if self.get_registered_user_details(email):
            return "Email exists"

        if password != cpassasword:
            return "Passwords dont match"
        else:
            if len(password) < 8:
                return "password length should be atleast 8 characters"

        self.users[email] = {'username': username,
                             'email': email, 'password': password}
        return "Successfully created account"

    def user_login(self, email, password):
        """Method to login a particular user"""

        if not (email and password):
            return "empty email or password fields"

        if not self.get_registered_user_details(email):
            return "email not found"

        result = self.users[email]
        passwd = result['password']
        if passwd != password:
            return "Password mismatch"
        else:
            return "Success login"

    def get_registered_user_details(self, email):
        """Method to get registered user name and email using email
        checks if email exists in the users dictionary as key
        then returns the email and username stored under that email key
        """
        user_details = self.users[email] if email in self.users else False
        return user_details
