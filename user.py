import re

users = {}


class Users(object):
    """
      Users Class to handle  user functions like login and signup
      """

    def __init__(self, username=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.username = username
        self.email = email
        self.password = password

    def user_register(self, email, username, password, cpassasword):
        """ method that defines the elements required to create an account """
        regUsername = "[a-zA-Z0-9- .]+$"
        regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        regPassword = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if re.match(regUsername, username):
            if username != '' and email != '' and password != '' and cpassasword != '' and cpassasword != ' ':
                if username not in users.keys():
                    if email not in users.keys():
                        if password == cpassasword:
                            if re.search(regEmail, email):
                                if re.search(regPassword, password):
                                    users[email] = {'username': username,
                                                    'email': email,
                                                    'password': password,
                                                    }
                                    return 1
                                return 2
                            return 3
                        return 4
                    return 5
                return 6
            return 7
        return 8

    def user_login(self, email, password):
        """Method to login user"""
        if email != '' and password != '':
            if email in users.keys():
                res = users[email]
                passwd = res['password']
                if passwd == password:
                    return 1
                return 2
            return 3
        return 4

    def get_username(self, email):
        if email in users.keys():
            resUser = users[email]
            return resUser['username']
        return False

    def get_email(self, email):
        if email in users.keys():
            resEmail = users[email]
            return resEmail['email']
        return False
