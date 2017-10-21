import os
from flask import render_template,request, session, g,Flask, url_for
from user import Users
from recipe import Recipe
app = Flask(__name__)
from app import app


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
        member = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        res = new_user.member_register(email, member, password, cpassword)
        if res == 1:
            session['user'] = member
            msg_output = "Successfully created Account"
            return render_template('login.html', success=msg_output)
        elif res == 7:
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)

        elif res == "205,Regex mismatch":
            msg_output = "Special characters are not allowed in member field"
            return render_template("registration.html", msg=msg_output)

        elif res == 2:
            msg_output = "Password should have atleat 8 characters with at least a letter and a number"
            return render_template("registration.html", msg=msg_output)

        elif res == 6:
            msg_output = "member name already taken"
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
            member = new_user.get_member(email)
            email = new_user.get_email(email)
            session['user'] = member
            session['email'] = email
            message = "login successful"
            return render_template("recipe-categories.html", success=message)

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
    return render_template("login.html")

@app.route('/cat_register', methods=['GET', 'POST'])
def category_register():
    """ Method to create a category """
    if g.user:
        if request.method == "POST":
            cat_name = request.form['category_name']
            owner = request.form['category_owner']
            category_create = new_cat.category_register(cat_name,owner)

            category_data = new_cat.recipe_categories
            render_category = []
            for category in category_data:
                if category_data[category]['owner'] == owner:
                    render_category.append(category)
                    if render_category == []:
                        url_for('/recipe-categories')

            if category_create == "200,OK":
                message = "Successfully created category"
                return render_template("recipe-categories.html", success=message, data=category_data)
            elif category_create == "204,Category exists":
                message = "Category exists"
                return render_template("recipe-categories.html", msg=message)
            elif category_create == "205,Invalid Name":
                message = "Invalid Category Name"
                return render_template("recipe-categories.html", msg=message)
            else:
                message = "unable to create category"
                return render_template("recipe-categories", msg=message)

    return render_template("login.html")



