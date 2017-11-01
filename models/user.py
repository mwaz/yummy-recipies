import re

users = {}
users['mwaz@gmail.com'] = {'username': 'mwaz', 'email': 'mwaz@gmail.com', 'password': '1234567q'}
regex_username = "[a-zA-Z0-9- .]+$"
regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class Users(object):
    """
    Users Class to handle  user functions like login and signup
    """
    
    def __init__(self, username=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.username= username
        self.email = email
        self.password = password

    def user_register(self, email, username, password, cpassasword):
        """ method that defines the elements required
         to create a member account
        """
        if not  (username and email and password and cpassasword):
            return "205,Invalid input"

        if not re.search(regex_username, username):
            return "205,Regex mismatch"

        if username in users.keys():
            return "401,username exists"
        
        if not re.search(regEmail, email):
            return "205,Email Regex mismatch"

        if email in users.keys():
            return "401,Email exists"    

        if password != cpassasword:
            return "400,Passwords dont match"
        else:
            if len(password) < 8:
                return "205,Password Regex mismatch"

        
        users[email] = {'username': username, 'email': email, 'password': password}
        print (users)
        return "200,OK"

    def user_login(self, email, password):
        """Method to login member"""

        if not (email and password):
            return "205,Empty input"
        if email not in users.keys():
            return "404,User not found"
        
        result = users[email]
        passwd = result['password']
        if passwd != password:
            return "205,Password mismatch"
        else:
            return "200,OK"

    def  get_registered_user_email(self, email):
        user_details = users[email] if email in users.keys() else False
        return user_details['email']

    def  get_registered_user_name(self, email):
        user_details = users[email] if email in users.keys() else False
        return user_details['username']
