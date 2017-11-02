import os
from flask import render_template, request, session, g, Flask
from models.user import Users
from models.recipe import Recipe
from models.categories import Categories
app = Flask(__name__)
from app import app

app.secret_key = os.urandom(24) #needed to keep the client sessions secure

new_user = Users() #instance of class Users
new_cat = Categories() #instance of class Category
new_recipe = Recipe() #instance of class Recipe


@app.route('/')
def index():
    """ Redirects to the index page """
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ 
    Handles the view for user registration, it then fetches 
    the return messages in the register methods and returns appropriate
    messages to the user through the templates
    """
    if request.method == "POST":
        #gets the email, password, password and confirm password from the
        #registration.html template
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        #result stores the result from the method user-register
        #present in the Users class 
        #the return statements given out are then emedded on the result variable
        #then returned to the user in the registration or login templates
        #depending on the result
        result = new_user.user_register(email, username, password, cpassword)
        if result == "Successfully created account":
            session['user'] = username
            msg_output = "Successfully created Account"
            return render_template('login.html', success=msg_output)

        elif result == "please input all fields":
            msg_output = "please fill in all the fields"
            return render_template("registration.html", msg=msg_output)

        elif result == "username should not have special characters or spaces":
            msg_output = "Special characters are not allowed in username field"
            return render_template("registration.html", msg=msg_output)

        elif result == "password length should be atleast 8 characters":
            msg_output = "Password should have atleat 8 characters"
            return render_template("registration.html", msg=msg_output)

        elif result == "username exists":
            msg_output = "user name already taken"
            return render_template("registration.html", msg=msg_output)

        elif result == "Passwords dont match":
            msg_output = "Passwords dont match"
            return render_template("registration.html", msg=msg_output)

        elif result == "Email format is invalid":
            msg_output = "Email is not a valid email in the format someone@someone.com"
            return render_template("registration.html", msg=msg_output)

        elif result == "Email exists":
            msg_output = "Email already exists"
            return render_template("registration.html", msg=msg_output)

    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the requests for the login view"""
    if request.method == "POST":
        #obtains the email and password in the login templates
        #calls the user_login method in the USER class using the new_cat instance
        #The status codes are returned and embedded in result_login and are used
        #to return messages to the login or recipe_categories templates
        email = request.form['email']
        password = request.form['password']
        result_login = new_user.user_login(email, password)

        if result_login == "Success login":
            username = new_user.get_registered_user_details(email)
            email = new_user.get_registered_user_details(email)
            session['user'] = username['username']

            session['email'] = email['email']
            message = "login successful"

            #method in the Users class to display all the recipe categories of a user
            data = new_cat.view_recipe_category(session['user'])

            if data is not None:
                return render_template("recipe-categories.html", success=message, data=data)
            else:
                return render_template("recipe-categories.html")

        elif result_login == "Password mismatch":
            message = "Invalid login credentials"
            return render_template("login.html", msg=message)

        elif result_login == "email not found":
            message = "User does not exist, kindly try again"
            return render_template("login.html", msg=message)

        elif result_login == "empty email or password fields":
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
        #sets the g.owner to the particular owner who has the sessions
        #using the username provided in the login method
        g.owner = session['user']

@app.route('/cat_register', methods=['GET', 'POST'])
def category_register():
    """ Method to create a category """
    #the method will only execute if there is a session present
    if g.owner:
        if request.method == "POST":
            cat_name = request.form['category_name']
            owner = g.owner
            category_create = new_cat.category_register(cat_name, owner)
            category_data = new_cat.view_recipe_category(g.owner)

            if category_create == "Successfully created category":
                message = "Successfully created category"
                return render_template("recipe-categories.html", success=message, data=category_data)
            
            elif category_create == "Category exists":
                message = "Category exists"
                return render_template("recipe-categories.html", msg=message, data=category_data)
            
            elif category_create == "Category name is null":
                message = "Kndly enter the category name"
                return render_template("recipe-categories.html", msg=message, data=category_data)
            
            elif category_create == "category name has special characters":
                message = "Category name should only have letters"
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
    """
    method to view the recipes that belong to the same category
    with the same owner
    """
    if g.owner:
        #The category name is obtained from the recipe_categories.html templates using GET
        category_name = category_name
        view_cat = new_recipe.view_recipe(category_name, g.owner)
        return render_template("recipes.html", message=category_name, data=view_cat)
    return render_template("login.html")



@app.route('/category_edit/<category_name>', methods=['GET', 'POST'])
def category_edit(category_name):
    """method to edit a recipe category """
    if g.owner:
        if request.method == "POST":
            cat_name = category_name
            new_cat_name = request.form['cat_name']
            category_result = new_cat.category_edit(cat_name, new_cat_name, g.owner)
            data = new_cat.view_recipe_category(g.owner)
            
            if category_result == "successfully updated category name":
                message = "Successfully edited category"
                return render_template("recipe-categories.html", success=message, data=data)

            elif category_result == "Category exists":
                message = "Can't edit category! Category Name Exists"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif category_result == "Null category name":
                message = "Category name is NOT provided"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif category_result == "category name exists":
                message = "Category Name exists"
                return render_template("recipe-categories.html", msg=message, data=data)

            elif category_result == "category name has special characters":
                message = "Category name should only have letters"
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

            if delete_result == "successfully deleted category":
                msg = "Recipe Category Deleted"
                return render_template("recipe-categories.html", msg=msg, data=data)
            elif delete_result == "Category doesnt exist":
                msg = "Recipe category does not exist"
                return render_template("recipe-categories.html", msg=msg, data=data)
            else:
                msg = "Can't delete category"
                return render_template("recipe-categories.html", msg=msg, data=data)
        return render_template("recipe-categories.html")
    return render_template("login.html")


@app.route('/recipe_register', methods=['GET', 'POST'])
def recipe_register():
    """method to create a recipe """
    #executes if the logged in user has a current session
    if g.owner:
        if request.method == "POST":
            recipe_name = request.form['recipe_name']
            cat_name = request.form['category_name']
            recipe_ingredients = request.form['recipe_ingredients']
            owner = g.owner
            recipe_create = new_recipe.recipe_register(cat_name, recipe_name, owner, recipe_ingredients)

            render_recipe = new_recipe.view_recipe(cat_name, g.owner)
            if recipe_create == "successfully created recipe":
                message = "Successfully created recipe"
                return render_template("recipes.html", success=message, data=render_recipe, message=cat_name)
            
            elif recipe_create == "Recipe exists":
                message = "Recipe exists"
                return render_template("recipes.html", msg=message, data=render_recipe, message=cat_name)
            
            elif recipe_create == "Null recipe name":
                message = "Recipe name is NOT provided"
                return render_template("recipes.html", msg=message, data=render_recipe, message=cat_name)
            
            elif recipe_create == "Null recipe ingredients":
                message = "Kindly provide recipe ingridients for the recipe"
                return render_template("recipes.html", msg=message, data=render_recipe, message=cat_name)
            

            elif recipe_create == "Recipe name has special characters":
                message = "Recipe Name should only have letters "
                return render_template("recipes.html", msg=message, data=render_recipe, message=cat_name)
            
            else:
                message = "unable to create recipe"
                return render_template("recipes.html", msg=message, data=render_recipe, message=cat_name)
        return render_template("recipes.html")
    return render_template("login.html")



@app.route('/recipe_delete', methods=['GET', 'POST'])
def recipe_delete():
    """method to delete a recipe"""
    if g.owner:
        if request.method == "POST":
            data = request.form['categor_name']
            recipe_name = request.form['recipe_name']
            delete_result = new_recipe.recipe_delete(recipe_name, data, g.owner)
            recipe_data = new_recipe.view_recipe(data, g.owner)

            if delete_result == "Successfully deleted recipe":
                msg = "Recipe Deleted"
                return render_template("recipes.html", msg=msg, message=data, data=recipe_data)      
            
            else:
                msg = "unable to delete recipe"
                return render_template("recipes.html", msg=msg, message=data, data=recipe_data)
        return render_template("recipes.html")
    return render_template("login.html")


@app.route('/recipe_edit/<category_name>', methods=['GET', 'POST'])
def recipe_edit(category_name):
    """method to edit a recipe """
    if g.owner:
        cat_name = category_name
        owner = g.owner
        data = new_recipe.view_recipe(cat_name, owner)
        recipe_name = request.form['recipe_name']
        recipe_ingredients = request.form['recipe_ingredients']

        if request.method == "POST":
            new_recipe_name = request.form['new_recipe_name']
            edit_recipe = new_recipe.recipe_edit(new_recipe_name, recipe_name, cat_name, owner, recipe_ingredients)

            if edit_recipe == "Successfully edited recipe":
                message = "Successfully edited recipe"
                return render_template("recipes.html",  message=cat_name, success=message, data=data)

            elif edit_recipe == "Recipe exists":
                error = "Can't edit Recipe! Recipe Name Exists"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            elif edit_recipe == "Null recipe name":
                error = "Invalid Recipe name"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            elif edit_recipe == "Recipe name has special characters":
                error = "Recipe name should only have letters"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

            else:
                error = "unable to edit recipe"
                return render_template("recipes.html", message=cat_name, msg=error, data=data)

        return render_template("recipes.html", message=cat_name, data=data)
    return render_template("login.html")

@app.route('/logout')
def logout():
    """ method to logout a user"""
    session.pop('user', None)
    return render_template("login.html")