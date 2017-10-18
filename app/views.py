import os
from flask import Flask, render_template, redirect, request, session
from flask import Flask
app = Flask(__name__)
from user import Users

new_user = Users()
"""Objects Instatiation"""
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    """ Redirects to the index page """

    return render_template('index.html')


@app.route('/register', methods=['GET','POST'])
def register():
    """ Handles the ciew for user registration"""
    if request.method == "POST":
        email = request.form['email']
        print(email)
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        res = new_user.user_register(email, username, password, cpassword)
        if res == 1:
            session['user'] = username
            msg_output = "Successfully created Account"

            return render_template('login.html', msg=msg_output)
        elif res == 7:
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)

        elif res == 8:
            msg_output = "Special characters are not allowed in username"
            return render_template("registration.html", msg=msg_output)

        elif res == 2:
            msg_output = "Password should have atleat 8 characters with at least a letter and a number"
            return render_template("registration.html", msg=msg_output)

        elif res == 6:
            msg_output = "Username already taken"
            print("5")
            return render_template("registration.html", ms=msg_output)
        elif res == 4:
            msg_output = "Passwords dont match"
            return render_template("registration.html", msg=msg_output)

        elif res == 3:
            msg_output = "Email is not a valid email in the format someone@someone.com"
            return render_template("registration.html", msg=msg_output)

        elif res == 5:
            msg_output = "Email already exists"
            return render_template("registration.html", msg=msg_output)

    return render_template("registration.html")

@app.route('/login')
def login():
    return render_template('login.html')


