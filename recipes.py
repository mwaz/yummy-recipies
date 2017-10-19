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

    def delete(self, recipe_category):
        """ method to delete a recipe category"""
        if recipe_category in self.Recipes.keys():
            # checks if the recipe_category being deleted exists
            if Recipeitems:
                for dic in range(0, len(Recipeitems)):
                    if Recipeitems[dic]['recipe_category'] == recipe_category:
                        del Recipeitems[dic]['recipe']
                        del Recipeitems[dic]['recipe_category']
                        del Recipeitems[dic]['recipes_owner']
                        del self.Recipes[recipe_category]
                        return 1
                return 2
            else:
                del self.Recipes[recipe_category]
                return 1
        return 2

    def get_recipe_categories(self):
        """ Method definition on how to retrieve recipe categories"""
        return self.Recipes


    def get_recipe_category(self,recipe_category):
        """Method definition to get a single recipe category"""
        return self.Recipes[recipe_category]

    def edit(self, old, recipe_category, recipes_owner):
        """Method to edit a recipe category"""
        if re.match("[a-zA-Z0-9- .]+$", recipe_category):
            if recipe_category != '':
                if old in self.Recipes.keys():
                    del self.Recipes[old]
                    self.Recipes[recipe_category] = {'recipe_category': recipe_category, 'recipes_owner': recipes_owner}
                    return 1
                return 2
            return 3
        return 4


    @classmethod
    def createrecipes(cls, recipe, recipe_category, recipes_owner):
        """Method definition to create recipes in the recipe categories"""
        if re.match("[a-zA-Z0-9- .]+$", recipe):
            if recipe != '':
                recipe_category.append(
                    {'recipe_category': recipe_category, 'recipe': recipe, 'recipes_owner': recipes_owner })
                return 1
            return 2
        return 3


    @classmethod
    def getrecipes(cls):
        """ method definition to get a recipe from a recipe_category """
        return Recipeitems















