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

    def create (self, recipe_category, recipes_owner):
        """defining method to create  a recipe category"""
        if re.match("[a-zA-Z0-9- .]+$", recipe_category):
            if recipe_category != '':
                # call the get_recipes function that contains individual recipes
                recipe_categories = self.get_recipes(recipes_owner)
                if recipe_categories != {}: #returns all recipe categories
                    #check if a user has a recipes in a recipe category
                    if recipe_category not in recipe_categories.keys():
                        self.Recipes[recipe_category] = {"recipe_category": recipe_category, "recipes_owner": recipes_owner,}
                        return 1
                    return 2
                else:
                    #Users first recipe category
                    self.Recipes[recipe_category] = {"recipe_category": recipe_category, "recipes_owner": recipes_owner}
                    return 1
            return 3
        return 4


    def get_recipes(self, recipes_owner):
        """ Method to get a users recipe categories """
        data = self.recipe
        recipe_categories = {}
        for recipe_category in data.keys():
            #looping through the recipe categories
            recipes = data[recipe_category]
            recipes_owner = recipes['recipes_owner']
            if recipes_owner == recipes_owner:
                recipe_categories[recipes_owner] = {
                    "recipe_category" : recipe_category,
                    "recipes_owner" : recipes_owner
                }
            else:
                res =  recipe_categories
        return recipe_categories

    














