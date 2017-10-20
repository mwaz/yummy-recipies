import os
import random
from flask import render_template, redirect, request, session, g, url_for
from flask import Flask
app = Flask(__name__)
from user import Users
from recipe import Recipe
from app import app

category_id = random.choice(range(0, 50))
new_user = Users()
new_cat = Recipe()
"""Objects Instatiation"""
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    """ Redirects to the index page """

    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Handles the ciew for user registration"""
    if request.method == "POST":
        email = request.form['email']
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
            return render_template("registration.html", msg=msg_output)
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the requests for the login view"""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        resLogin = new_user.user_login(email, password)
        if resLogin == 1:
            username = new_user.get_username(email)
            email = new_user.get_email(email)
            session['user'] = username
            session['email'] = email
            message = "login successful"
            return render_template("recipe-categories.html", msg=message)

        elif resLogin == 2:
            message = "Passwords do not match"
            return render_template("login.html", msg=message)
        elif resLogin == 3:
            message = "User does not exist, kindly try again"
            return render_template("login.html", msg=message)
        elif resLogin == 4:
            message = "Kindly fill all fields"
            return render_template("login.html", msg=message)
        else:
            message = "Invalid credentials, try again"
            return render_template("login.html", msg=message)
    return render_template("login.html")


@app.before_request
def before_request():
    """Method to declare sessions"""
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/logout')
def logout():
    """ method to logout a user"""
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/cat_register', methods=['GET', 'POST'])
def category_register():
    """ Method to create a category """
    if request.method == "POST":
        cat_name = request.form['category_name']
        cat_id = request.form['category_name']
        owner = request.form['category_owner']

        category_create = new_cat .category_register(cat_name,cat_id, owner)
        if category_create == 1:
            message = "Successfully created category"
            return render_template("recipe-categories.html", msg=message)

        elif category_create == 2:
            message = "Category id already exists"
            return render_template("recipe-categories.html", msg=message)
        elif category_create == 3:
            message = "Category already exists"
            return render_template("recipe_categories", msg=message)
        elif category_create == 4:
            message = "Kindly input category name"
            return render_template("recipe_categories.html", msg=message)
        elif category_create == 5:
            message = "No special characters allowed in category name"
            return render_template("recipe_categories.html", msg=message)
        else:
            message = "unable to create category"
            return render_template("recipe_categories", msg=message)
    return render_template("recipe_categories.html")

