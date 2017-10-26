[![Build Status](https://travis-ci.org/mwaz/yummy-recipies.svg?branch=challenge_two)](https://travis-ci.org/mwaz/yummy-recipies)
[![Coverage Status](https://coveralls.io/repos/github/mwaz/yummy-recipies/badge.svg?branch=develop)](https://coveralls.io/github/mwaz/yummy-recipies?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/52e878916d0ff93df8be/maintainability)](https://codeclimate.com/github/mwaz/yummy-recipies/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/361f8c2f72e04e3c8a4fa6c18c84eb51)](https://www.codacy.com/app/mwaz/yummy-recipies?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mwaz/yummy-recipies&amp;utm_campaign=Badge_Grade)
[![License](http://img.shields.io/:license-mit-blue.svg)](https://github.com/mwaz/yummy-recipies/blob/challenge_two/licence.txt)

Andela Bootcamp challenge which provides a platform for users to keep track of their
awesome recipes and share with others if they so wish.

# Contains

The application contains the user interfaces for the yummy-recipies,

UML diagrams for the Project

The flask application for yummy-recipies

# Prerequisites

python 3.6 or a later python version is required to run this app.

# Installing
clone the repository

FOR HTTPS
https://github.com/mwaz/yummy-recipies

FOR SSH
git@github.com:mwaz/yummy-recipies.git

# Change Directory into the project folder

$ cd yummy-recipies

# Create a virtual environment with Python 3.6

$ virtualenv --python=python3.6 yourenvname

# Activate the virtual environment you have just created

$ source yourenvname/bin/activate

# Install the application's dependencies from requirements.txt to the virtual environment

$ (yourenvname) pip install -r requirements.txt

# Set up Unit Test Environment

run the following command to install nose unit testing environment:

$ (yourenvname) pip install nose

This will enable you to run sngle file tests like.

$ (yourenvname) nosetests -v

# Running the program

Run the program by typing the command in your terminal :

$  (yourenvname) python run.py
you can now use the application.

# Live App on heroku
https://yummy-recipies.herokuapp.com