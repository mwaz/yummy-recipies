from flask import Flask


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

#initialize views
from yummy_recipes.app import views

# Load the config file
app.config.from_object('config')