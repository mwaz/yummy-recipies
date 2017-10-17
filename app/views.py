from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recipe-categories')
def recipeCategories():
    return render_template('recipe-categories.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')




if __name__ == "__main__":
    app.run(debug=True)
