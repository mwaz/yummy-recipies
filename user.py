import re

users = {}
regex_member = "[a-zA-Z0-9- .]+$"
regEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
regPassword = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

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
        """ method that defines the elements required to create an account """
        if re.match(regex_member, member):
            if member != '' and email != '' and password != '' and cpassasword != '' and cpassasword != ' ':
                if member not in users.keys():
                    if email not in users.keys():
                        if password == cpassasword:
                            if re.search(regEmail, email):
                                if re.search(regPassword, password):
                                    users[email] = {'member': member,
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
        return "205,Regex mismatch"

    def user_login(self, email, password):
        """Method to login user"""
        if email != ' ' and password != ' ':
            if email != '' and password != '':
                if email in users.keys():
                    result = users[email]
                    passwd = result['password']
                    if passwd == password:
                        return 1
                    return 2
                return 3
            return 4
        return 5


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
