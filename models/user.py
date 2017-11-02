import re


class Users(object):
    """
    Users Class to handle  user functions like login and signup
    """
    #Dictionary to store the user details
    users = {}
    # storing a default user for testing purposes, avoiding signup on
    # every server restart
    users['mwaz@gmail.com'] = {'username': 'mwaz',
                               'email': 'mwaz@gmail.com', 'password': '1234567q'}

    # regex to check if the email entered follows the regex pattern
    regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    # regex to check if the username entered follows the regex pattern
    regex_name = "[a-zA-Z0-9- .]+$"

    def __init__(self, username=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password
        self.regex_username = "[a-zA-Z0-9- .]+$"

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

        if not (username and email and password and cpassasword):
            return "205,Invalid input"

        if not re.search(self.regex_username, username):
            return "205,Regex mismatch"

        if username in self.users.keys():
            return "401,username exists"

        if not re.search(self.regEmail, email):
            return "205,Email Regex mismatch"

        if email in self.users.keys():
            return "401,Email exists"

        if password != cpassasword:
            return "400,Passwords dont match"
        else:
            if len(password) < 8:
                return "205,Password Regex mismatch"

        self.users[email] = {'username': username,
                             'email': email, 'password': password}
        return "200,OK"

    def user_login(self, email, password):
        """Method to login a particular user"""

        if not (email and password):
            return "205,Empty input"

        if email not in self.users.keys():
            return "404,User not found"

        result = self.users[email]
        passwd = result['password']
        if passwd != password:
            return "205,Password mismatch"
        else:
            return "200,OK"

    def get_registered_user_email(self, email):
        """Method to get registered user name using email
        checks if email exists in the users dictionary as key
        then returns the email stored under that email key
        """
        user_details = self.users[email] if email in self.users.keys(
        ) else False
        return user_details['email']

    def get_registered_user_name(self, email):
        """
        Method to get registered user name using email
        checks if email exists in the users dictionary as key
        then returns the username stored under that email key
        """
        user_details = self.users[email] if email in self.users.keys(
        ) else False
        return user_details['username']
