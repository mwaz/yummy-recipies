import re
regex_name = "[a-zA-Z0-9- .]+$"


class Recipe(object):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
      """
    recipe_categories = {}
    recipes = {}

    def __init__(self, cat_name=None, owner=None, recipe_name=None):
        """ Initializing  class instance variables"""
        self.cat_name = cat_name
        self.owner = owner
        self.recipe_name = recipe_name

    def category_register(self, cat_name, owner):
        """ method that defines the elements required to create an account """
        if re.match(regex_name, cat_name):
            if cat_name != '' and cat_name.strip():
                if cat_name not in self.recipe_categories:
                    self.recipe_categories[cat_name] = {"cat_name": cat_name, "owner": owner}
                    return "200,OK"
                return "204,Category exists"
            return "205,Invalid Name"
        return "205,Regex mismatch"

    def category_delete(self, cat_name):
        """ method that defines the elements required to create an account """
        if cat_name in self.recipe_categories.keys():
            del self.recipe_categories[cat_name]
            if cat_name in self.recipes.keys():
                del self.recipes[cat_name:]
            return "200,OK"
        return "404,Category doesnt exist"

    def recipe_register(self, cat_name, recipe_name, owner):
        """ method that defines the elements required to create an account """
        if re.match(regex_name, cat_name):
            if recipe_name != '' and recipe_name.strip():
                if recipe_name not in self.recipes:
                    self.recipes[recipe_name] = {"cat_name": cat_name, "recipe_name": recipe_name, "owner": owner}
                    return "200,OK"
                return "204,Recipe exists"
            return "205,Invalid Name"
        return "205,Regex mismatch"

    def recipe_delete(self, recipe_name):
        """ method that defines the elements required to create an account """
        if recipe_name in self.recipes.keys():
            del self.recipes[0:]
            return "200,OK"
        return "404,Recipe doesnt exist"

    def view_recipe_category(self, owner):
        category_data = self.recipe_categories
        render_category = []
        for category in category_data:
            if category_data[category]['owner'] == owner:
                render_category.append(category)
        return render_category

    def view_recipe(self, cat_name):
        recipe_data = self.recipes
        render_recipe = []
        for recipe in recipe_data:
            if recipe_data[recipe]['cat_name'] == cat_name:
                render_recipe.append(recipe)
        return render_recipe
