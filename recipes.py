import re

Recipeitems = []
# an empty lists which stores recipes


class Recipe(object):
    Recipes = {}
    shared_recipes = {}

    def __init__(self, recipe_category = None, recipes_owner = None, recipe = None):
        """Initialization of recipe class variables"""

        self.recipe_category = recipe_category
        self.owner = recipes_owner
        self.recipe = recipe

   