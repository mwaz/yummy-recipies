import os
from flask import render_template, request, session, g, Flask
from yummy_recipes.models.user import Users
from yummy_recipes.models.recipe import Recipe
app = Flask(__name__)
from yummy_recipes.app import app

app.secret_key = os.urandom(24) #needed to keep the client sessions secure

new_user = Users() #instance of class Users
new_cat = Recipe() #instance of class Recipe


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
        result = new_user.user_register(email, username, password, cpassword)
        if result == "200,OK":
            session['user'] = username
            msg_output = "Successfully created Account"
            return render_template('login.html', success=msg_output)

        elif result == "205,Invalid input":
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)

        elif result == "205,Empty input":
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)


        elif result == "205,Regex mismatch":
            msg_output = "Special characters are not allowed in username field"
            return render_template("registration.html", msg=msg_output)

        elif result == "205,Password Regex mismatch":
            msg_output = "Password should have atleat 8 characters with at least a letter and a number and a special character"
            return render_template("registration.html", msg=msg_output)

        elif result == "401,username exists":
            msg_output = "member name already taken"
            return render_template("registration.html", msg=msg_output)

        elif result == "400,Passwords dont match":
            msg_output = "Passwords dont match"
            return render_template("registration.html", msg=msg_output)

        elif result == "205,Email Regex mismatch":
            msg_output = "Email is not a valid email in the format someone@someone.com"
            return render_template("registration.html", msg=msg_output)

        elif result == "401,Email exists":
            msg_output = "Email already exists"
            return render_template("registration.html", msg=msg_output)

    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the requests for the login view"""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        result_login = new_user.user_login(email, password)

        if result_login == "200,OK":
            username = new_user.get_registered_user_name(email)
            email = new_user.get_registered_user_email(email)
            session['user'] = username
            session['email'] = email
            message = "login successful"

            data = new_cat.view_recipe_category(session['user'])

            if data is not None:
                return render_template("recipe-categories.html", success=message, data=data)
            else:
                return render_template("recipe-categories.html")

        elif result_login == "205,Password match":
            message = "Invalid login credentials"
            return render_template("login.html", msg=message)

        elif result_login == "404,User not found":
            message = "User does not exist, kindly try again"
            return render_template("login.html", msg=message)

        elif result_login == "205,Empty Input":
            message = "Kindly fill all fields"
            return render_template("login.html", msg=message)
        else:
            message = "Invalid credentials, try again"
            return render_template("login.html", msg=message)
    return render_template("login.html")


@app.before_request
def before_request():
    """Method to declare sessions"""
    g.owner = None
    if 'user' in session:
        g.owner = session['user']

@app.route('/cat_register', methods=['GET', 'POST'])
def category_register():
    """ Method to create a category """
    if g.owner:
        if request.method == "POST":
            cat_name = request.form['category_name']
            owner = g.owner
            category_create = new_cat.category_register(cat_name, owner)
            category_data = new_cat.view_recipe_category(g.owner)

            if category_create == "200,OK":
                message = "Successfully created category"
                return render_template("recipe-categories.html", success=message, data=category_data)
            
            elif category_create == "200,OK,UPDATE":
                message = "Successfully updated category"
                return render_template("recipe-categories.html", success=message, data=category_data)

            elif category_create == "204,Category exists":
                message = "Category exists"
                return render_template("recipe-categories.html", msg=message, data=category_data)
            elif category_create == "205,Invalid Name":
                message = "Invalid Category Name"
                return render_template("recipe-categories.html", msg=message, data=category_data)
            else:
                message = "unable to create category"
                return render_template("recipe-categories.html", msg=message, data=category_data)
        else:
            category_data = new_cat.view_recipe_category(g.owner)
            return render_template("recipe-categories.html", data=category_data)
    return render_template("login.html")


@app.route('/view_category/<category_name>', methods=["POST", "GET"])
def view_category(category_name):
    if g.owner:
        category_name = category_name
        view_cat = new_cat.view_recipe(category_name, g.owner)
        return render_template("recipes.html", message=category_name, data=view_cat)
    return render_template("login.html")


@app.route('/recipe_register', methods=['GET', 'POST'])
def recipe_register():
    """method to create a recipe """
    if g.owner:
        if request.method == "POST":
            recipe_name = request.form['recipe_name']
            cat_name = request.form['category_name']
            owner = g.owner
            recipe_create = new_cat.recipe_register(cat_name, recipe_name, owner)
            render_category = new_cat.view_recipe(cat_name, g.owner)
            if recipe_create == "200,OK":
                message = "Successfully created recipe"
                return render_template("recipes.html", success=message, data=render_category, message=cat_name)
            elif recipe_create == "204,Recipe exists":
                message = "Recipe exists"
                return render_template("recipes.html", msg=message, data=render_category, message=cat_name)
            elif recipe_create == "205,Invalid Name":
                message = "Invalid Recipe Name"
                return render_template("recipes.html", msg=message, data=render_category, message=cat_name)
            elif recipe_create == "205,Regex mismatch":
                message = "Recipe Name has special characters "
                return render_template("recipes.html", msg=message, data=render_category, message=cat_name)
            else:
                message = "unable to create recipe"
                return render_template("recipes.html", msg=message, data=render_category, message=cat_name)
        return render_template("recipes.html")
    return render_template("login.html")


@app.route('/category_edit/<category_name>', methods=['GET', 'POST'])
def category_edit(category_name):
    """method to edit a recipe category """
    if g.owner:
        if request.method == "POST":
            cat_name = category_name
            new_cat_name = request.form['cat_name']
            recipe_edit = new_cat.category_edit(cat_name, new_cat_name, g.owner)
            data = new_cat.view_recipe_category(g.owner)

            # recipe_edit = new_cat.recipe_register(new_cat_name, owner)

            if recipe_edit == "200,OK":
                message = "Successfully edited category"
                return render_template("recipe-categories.html", success=message, data=data)

            if recipe_edit == "200,OK,UPDATE":
                message = "Successfully edited category"
                return render_template("recipe-categories.html", success=message, data=data)


            elif recipe_edit == "204,Category exists":
                message = "Can't edit category! Category Name Exists"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif recipe_edit == "205,Invalid Name":
                message = "Invalid category name"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif recipe_edit == "205,Regex mismatch":
                message = "Regex mismatch"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif recipe_edit == "404,Cant Edit Category":
                message = "Cannot Edit Category"
                return render_template("recipe-categories.html", msg=message, data=data)
            else:
                message = "unable to edit recipe category"
                return render_template("recipe-categories.html", msg=message, data=data)
        return render_template("recipe-categories.html")
    return render_template("login.html")


@app.route('/category_delete', methods=['GET', 'POST'])
def category_delete():
    """method to delete a recipe category """
    if g.owner:
        if request.method == "POST":
            category_name = request.form['category_name']
            delete_result = new_cat.category_delete(category_name, g.owner)
            data = new_cat.view_recipe_category(g.owner)

            if delete_result == "200,OK":
                msg = "Recipe Category Deleted"
                return render_template("recipe-categories.html", msg=msg, data=data)
            elif delete_result == "404,Category doesnt exist":
                msg = "Recipe category does not exist"
                return render_template("recipe-categories.html", msg=msg, data=data)
            else:
                msg = "Can't delete category"
                return render_template("recipe-categories.html", msg=msg, data=data)
        return render_template("recipe-categories.html")
    return render_template("login.html")


@app.route('/recipe_delete', methods=['GET', 'POST'])
def recipe_delete():
    """method to delete a recipe"""
    if g.owner:
        if request.method == "POST":
            data = request.form['categor_name']
            recipe_name = request.form['recipe_name']
            delete_result = new_cat.recipe_delete(recipe_name, data, g.owner)
            recipe_data = new_cat.view_recipe(data, g.owner)

            if delete_result == "200,OK":
                msg = "Recipe Deleted"
                return render_template("recipes.html", msg=msg, message=data, data=recipe_data)
            elif delete_result == "404,Recipe doesnt exist":
                msg = "Recipe does not exist"
                return render_template("recipes.html", msg=msg, message=data, data=recipe_data)
            else:
                msg = "Can't delete recipe"
                return render_template("recipes.html", msg=msg, message=data, data=recipe_data)
        return render_template("recipes.html")
    return render_template("login.html")


@app.route('/recipe_edit/<category_name>', methods=['GET', 'POST'])
def recipe_edit(category_name):
    """method to edit a recipe """
    if g.owner:
        cat_name = category_name
        owner = g.owner
        data = new_cat.view_recipe(cat_name, owner)
        recipe_name = request.form['recipe_name']
        if request.method == "POST":
            new_recipe_name = request.form['new_recipe_name']
            edit_recipe = new_cat.recipe_edit(new_recipe_name, recipe_name, cat_name, owner)

            if edit_recipe == "200,OK":
                message = "Successfully edited recipe"
                return render_template("recipes.html",  message=cat_name, success=message, data=data)

            elif edit_recipe == "204,Recipe exists":
                error = "Can't edit Recipe! Recipe Name Exists"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            elif edit_recipe == "205,Invalid Name":
                error = "Invalid Recipe name"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            elif edit_recipe == "205,Regex mismatch":
                error = "Regex mismatch"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            elif edit_recipe == "401,Process error":
                error = "Cannot Edit Recipe, Invalid token"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)
            else:
                error = "unable to edit recipe "
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

        return render_template("recipes.html", message=cat_name, data=data)
    return render_template("login.html")

@app.route('/logout')
def logout():
    """ method to logout a user"""
    session.pop('user', None)
    return render_template("login.html")