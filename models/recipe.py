"""Class to create, edit, delete recipes"""
import re

from models.user import Users

# class Recipe inherits from the User class, where every method present
# in the Users class can be used in the Recipes class


class Recipe(Users):
    """
      Recipe Class to handle methods to do with recipes
    """
    
    def __init__(self, cat_name=None, owner=None, recipe_name=None, recipe_ingredients=None, recipe_methods=None):
        """ Initializing Recipe class instance variables"""
        self.cat_name = cat_name
        self.owner = owner
        self.recipe_name = recipe_name
        self.regex_name = "[a-zA-Z- .]+$"
        self.recipes = []
        self.recipe_ingredients = recipe_ingredients
        self.recipe_methods = recipe_methods

    def recipe_register(self, cat_name, recipe_name, owner, recipe_ingredients, recipe_methods):
        """ method that defines the elements required to create an account """
        if recipe_name:
            recipe_name = re.sub(r'\s+', ' ', recipe_name).strip()

        recipe_name = None if recipe_name == " " else recipe_name.title()

        if recipe_ingredients:
            recipe_ingredients = re.sub(
                r'\s+', ' ', recipe_ingredients).strip()

        recipe_ingredients = None if recipe_ingredients == " " else recipe_ingredients

        if recipe_methods:
            recipe_methods = re.sub(
                r'\s+', ' ', recipe_methods).strip()

        recipe_methods = None if recipe_methods == " " else recipe_methods

        if not recipe_name:
            return "Null recipe name"

        if not recipe_ingredients:
            return "Null recipe ingredients"

        if not recipe_methods:
            return "Null recipe method"

        if not re.search(self.regex_name, recipe_name):
            return "Recipe name has special characters"

        if (any(recipe_name == recipe_list[1]
                and owner == recipe_list[2]
                and cat_name == recipe_list[0]
                for recipe_list in self.recipes)) is True:
            # returns an error if the recipe name is in the same category
            # and having the same owner

            return "Recipe exists"


        # if the recipe name meets the condition it is added to the recipes list
        self.recipes.append([cat_name, recipe_name, owner, recipe_ingredients, recipe_methods])
        return "successfully created recipe"

    def recipe_edit(self, new_recipe_name, recipe_name, cat_name, owner, recipe_ingredients, recipe_methods):
        """ method that defines how to edit a recipe, the method takes
        the new recipe name as a parameter, the recipe name and the category
        name, all belonging to the logged in user"""
        if new_recipe_name:
            new_recipe_name = re.sub(r'\s+', ' ', new_recipe_name).strip()

        new_recipe_name = None if new_recipe_name == " " else new_recipe_name

        if recipe_ingredients:
            recipe_ingredients = re.sub(
                r'\s+', ' ', recipe_ingredients).strip()

        recipe_ingredients = None if recipe_ingredients == " " else recipe_ingredients

        if recipe_methods:
            recipe_methods = re.sub(
                r'\s+', ' ', recipe_methods).strip()

        recipe_methods = None if recipe_methods == " " else recipe_methods


        if not new_recipe_name:
            return "Null recipe name"

        if not re.search(self.regex_name, new_recipe_name):
            return "Recipe name has special characters"

        for recipe_list in self.recipes:

            # checks to find if the new recipe name exists in the recipes list
            if (any(new_recipe_name == recipe_list[1] for
                    recipe_list in self.recipes)) is True:

                return "Recipe exists"

        recipe_list[1] = new_recipe_name

        if recipe_ingredients:
            recipe_list[3] = recipe_ingredients

        if recipe_methods:
            recipe_list[4] = recipe_methods

        return "Successfully edited recipe"

    def recipe_delete(self, recipe_name, cat_name, owner):
        """ method that defines the elements required to delete a recipe """
        for recipe_list in self.recipes:
            if recipe_list[1] == recipe_name and recipe_list[0] == cat_name:
                recipe_index = self.recipes.index(recipe_list)
                del self.recipes[recipe_index]
                return "Successfully deleted recipe"
        return "unable to delete recipe"

    def delete_category_recipes(self, cat_name, owner):
        """ delete all the recipes for a specific category """
        for recipe_list in self.recipes:
            recipe_index = self.recipes.index(recipe_list)
            del self.recipes[recipe_index]
            return "Successfully deleted recipe"
        return "unable to delete recipe"

    def view_recipe(self, cat_name, owner):
        """method to view all the recipes that belong to a category
        with the same owner"""
        recipe_data = self.recipes
        render_recipe_data = []
        for recipe in recipe_data:
            if recipe[0] == cat_name and recipe[2] == owner:
                render_recipe_data.append(recipe)
        return render_recipe_data
