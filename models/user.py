import re

users = {}
regex_member = "[a-zA-Z0-9- .]+$"
regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"



class Users(object):
    """
      Users Class to handle  user functions like login and signup
      """
    def __init__(self, member=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.member = member
        self.email = email
        self.password = password

    def member_register(self, email, member, password, cpassasword):
        """ method that defines the elements required
         to create a member account
          """
        if re.match(regex_member, member):
            if member != '' and email != '' and password != '' and cpassasword != '' and cpassasword != ' ':
                if member not in users.keys():
                    if email not in users.keys():
                        if password == cpassasword:
                            if re.search(regEmail, email):
                                if len(password) >= 8:
                                    users[email] = {'member': member, 'email': email, 'password': password}
                                    return "200,OK"
                                return "205,Password Regex mismatch"
                            return "205,Email Regex mismatch"
                        return "400,Passwords dont match"
                    return "401,Email exists"
                return "401,Member exists"
            return "205,Invalid input"
        return "205,Regex mismatch"


    def get_member(self, email):
        if email in users.keys():
            result_user = users[email]
            return result_user['member']
        return False

    def get_email(self, email):
        if email in users.keys():
            result_email = users[email]
            return result_email['email']
        return False

    def user_login(self, email, password):
        """Method to login member"""
        if email != ' ' and password != ' ':
            if email != '' and password != '':
                if email in users.keys():
                    result = users[email]
                    passwd = result['password']
                    if passwd == password:
                        return "200,OK"
                    return "205,Password mismatch"
                return "404,User not found"
            return "205,Invalid input"
        return "205,Empty input"