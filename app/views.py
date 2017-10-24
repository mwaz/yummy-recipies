import os
from flask import render_template, request, session, g, Flask, url_for
from models.user import Users
from models.recipe import Recipe
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
        result = new_user.member_register(email, member, password, cpassword)
        if result == "200,OK":
            session['user'] = member
            msg_output = "Successfully created Account"
            return render_template('login.html', success=msg_output)
        elif result == "205,Invalid input":
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)

        elif result == "205,Regex mismatch":
            msg_output = "Special characters are not allowed in member field"
            return render_template("registration.html", msg=msg_output)

        elif result == "205,Password Regex mismatch":
            msg_output = "Password should have atleat 8 characters with at least a letter and a number"
            return render_template("registration.html", msg=msg_output)

        elif result == "401,Member exists":
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
            member = new_user.get_member(email)
            email = new_user.get_email(email)
            session['user'] = member
            session['email'] = email
            message = "login successful"

            data = new_cat.view_recipe_category(session['user'])
            print(data)
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
        elif result_login == "205,Invalid input":
            message = "Kindly fill all fields"
            return render_template("login.html", msg=message)
        else:
            message = "Invalid credentials, try again"
            return render_template("login.html", msg=message)
    return render_template("login.html")


@app.before_request
def before_request():
    """Method to declare sessions"""
    g.member = None
    if 'user' in session:
        g.member = session['user']


@app.route('/logout')
def logout():
    """ method to logout a user"""
    session.pop('user', None)
    return render_template("login.html")


@app.route('/cat_register', methods=['GET', 'POST'])
def category_register():
    """ Method to create a category """
    if g.member:
        if request.method == "POST":
            cat_name = request.form['category_name']
            owner = g.member
            category_create = new_cat.category_register(cat_name, owner)
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
                return render_template("recipe-categories.html", msg=message, data=category_data)
            elif category_create == "205,Invalid Name":
                message = "Invalid Category Name"
                return render_template("recipe-categories.html", msg=message, data=category_data)
            else:
                message = "unable to create category"
                return render_template("recipe-categories.html", msg=message, data=category_data)
        else:
            category_data = new_cat.recipe_categories
            render_category = []
            for category in category_data:
                if category_data[category]['owner'] == g.member:
                    render_category.append(category)
                    if render_category == []:
                        url_for('/recipe-categories')

            return render_template("recipe-categories.html", data=category_data)

    return render_template("login.html")


@app.route('/view_category', methods=["POST", "GET"])
def view_category():
    if g.member:

        category_name = request.form['category_name']
        view_cat = new_cat.view_recipe_category(category_name)
        print(view_cat)

        return render_template("recipes.html", message=category_name, data=view_cat)
    return render_template("login.html")


@app.route('/recipe_register', methods=['GET', 'POST'])
def recipe_register():
    """method to create a recipe """
    if g.member:
        if request.method == "POST":
            recipe_name = request.form['recipe_name']
            cat_name = request.form['category_name']
            owner = g.member

            recipe_create = new_cat.recipe_register(cat_name, recipe_name, owner)

            category_name = cat_name
            recipe_data = new_cat.recipes
            render_recipe = []
            for recipe in recipe_data:
                if recipe_data[recipe]['cat_name'] == cat_name:
                    render_recipe.append(recipe)

            if recipe_create == "200,OK":
                message = "Successfully created recipe"
                return render_template("recipes.html", success=message, data=render_recipe, message=category_name)
            elif recipe_create == "204,Recipe exists":
                message = "Recipe exists"
                return render_template("recipes.html", msg=message, data=recipe_data)
            elif recipe_create == "205,Invalid Name":
                message = "Invalid Recipe Name"
                return render_template("recipes.html", msg=message, data=recipe_data)
            elif recipe_create == "205,Regex mismatch":
                message = "Recipe Name has special characters "
                return render_template("recipes.html", msg=message, data=recipe_data)
            else:
                message = "unable to create recipe"
                return render_template("recipes.html", msg=message, data=recipe_data)
        return render_template("recipes.html")
    return render_template("login.html")


@app.route('/category_edit', methods=['GET', 'POST'])
def category_edit():
    """method to edit a recipe category """
    if g.member:
        if request.method == "POST":
            recipe_name = request.form['recipe_name']
            cat_name = request.form['category_name']
            owner = g.member

            recipe_create = new_cat.recipe_register(cat_name, recipe_name, owner)

            if recipe_create == "200,OK":
                message = "Successfully created recipe"
                return render_template("recipes.html", success=message)
            elif recipe_create == "204,Recipe exists":
                message = "Recipe exists"
                return render_template("recipes.html", msg=message)
            elif recipe_create == "205,Invalid Name":
                message = "Invalid Recipe Name"
                return render_template("recipes.html", msg=message)
            elif recipe_create == "205,Regex mismatch":
                message = "Recipe Name has special characters "
                return render_template("recipes.html", msg=message)
            else:
                message = "unable to create recipe"
                return render_template("recipes.html", msg=message)
        return render_template("recipes.html")
    return render_template("login.html")


@app.route('/category_delete', methods=['GET', 'POST'])
def category_delete():
    """method to delete a recipe category """
    if g.member:
        if request.method == "POST":
            recipe_name = request.form['category_name']
            delete_result = new_cat.category_delete(recipe_name)
            data = new_cat.view_recipe_category(g.member)
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
    if g.member:
        if request.method == "POST":
            data = request.form['categor_name']
            recipe_name = request.form['recipe_name']
            delete_result = new_cat.recipe_delete(recipe_name)
            recipe_data = new_cat.view_recipe(data)

            if delete_result == "200,OK":
                msg = "Recipe Deleted"
                return render_template("recipes.html", msg=msg, message=data, recipes=recipe_data)
            elif delete_result == "404,Recipe doesnt exist":
                msg = "Recipe does not exist"
                return render_template("recipes.html", msg=msg, message=data, recipes=recipe_data)
            else:
                msg = "Can't delete category"
                return render_template("recipes.html", msg=msg, message=data, recipes=recipe_data)
        return render_template("recipes.html")
    return render_template("login.html")
