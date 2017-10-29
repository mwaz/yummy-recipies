import re
regex_name = "[a-zA-Z0-9- .]+$"


class Recipe(object):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
      """
    recipe_categories = []
    recipes = []

    def __init__(self, cat_name=None, owner=None, recipe_name=None):
        """ Initializing  class instance variables"""
        self.cat_name = cat_name
        self.owner = owner
        self.recipe_name = recipe_name

    def category_register(self, cat_name, owner):
        """ method that defines the elements required to create an account """
        if re.match(regex_name, cat_name):
            if cat_name != '' and cat_name.strip():
                if self.recipe_categories != []:
                    if (any(cat_name == category_list[0] and owner == category_list[1]
                            for category_list in self.recipe_categories)) != True:
                        self.recipe_categories.append([cat_name, owner,])
                        return "200,OK"
                    return "204,Category exists"
                self.recipe_categories.append([cat_name, owner, ])
                return "200,OK"
            return "205,Invalid Name"
        return "205,Regex mismatch"

    def category_edit(self, cat_name, new_cat_name, owner):
        """ method that defines the elements required delete a category """
        if new_cat_name != '' and new_cat_name.strip():
            if re.match(regex_name, new_cat_name):
                for category_list in self.recipe_categories:
                    if category_list[0] == cat_name and category_list[1] == owner:
                        if (any(new_cat_name == category_list[0]
                                for category_list in self.recipe_categories)) != True:
                            category_list[0] = new_cat_name

                            return "200,OK"
                        return "204,Category exists"
                    return "205,Invalid Name"
            return "205,Regex mismatch"
        return "205,Invalid Name"

    def category_delete(self, cat_name, owner):
        """ method that defines the elements required delete a category """
        for category_list in self.recipe_categories:
            if category_list[0] == cat_name and category_list[1] == owner:
                category_index = self.recipe_categories.index(category_list)
                self.recipe_categories.pop(category_index)
                return "200,OK"
            # return "404,Category doesnt exist"

    def recipe_register(self, cat_name, recipe_name, owner):
        """ method that defines the elements required to create an account """
        if re.match(regex_name, cat_name):
            if recipe_name != '' and recipe_name.strip():
                if self.recipes != []:
                    if (any(recipe_name == recipe_list[1] and owner == recipe_list[2]
                            and cat_name == recipe_list[0]
                            for recipe_list in self.recipes)) != True:
                        self.recipes.append([cat_name, recipe_name, owner, ])
                        return "200,OK"
                    return "204,Recipe exists"
                self.recipes.append([cat_name, recipe_name, owner])
                return "200,OK"
            return "205,Invalid Name"
        return "205,Regex mismatch"

    def recipe_edit(self, new_recipe_name, cat_name, owner):
        """ method that defines the elements required to edit a recipe"""
        if new_recipe_name != '' and new_recipe_name.strip():
            if re.match(regex_name, new_recipe_name):
                for recipe_list in self.recipes:
                    recipe_index = self.recipes.index(recipe_list)
                    if (any(new_recipe_name == recipe_list[1]
                            for recipe_list in self.recipes)) != True:
                        self.recipes[recipe_index][1] = new_recipe_name
                        return "200,OK"
                    return "204,Recipe exists"
            return "205,Regex mismatch"
        return "205,Invalid Name"

    def recipe_delete(self, recipe_name, cat_name, owner):
        """ method that defines the elements required to delete a recipe """
        for recipe_list in self.recipes:
            if recipe_list[1] == recipe_name and recipe_list[0] == cat_name and owner :
                recipe_index = self.recipes.index(recipe_list)
                del self.recipes[recipe_index]
                return "200,OK"

    def view_recipe_category(self, owner):
        category_data = self.recipe_categories
        render_category = []
        for category in category_data:
            if category[1] == owner:
                render_category.append(category)
        return render_category

    def view_recipe(self, cat_name, owner):
        recipe_data = self.recipes
        render_recipe = []
        for recipe in recipe_data:
            if recipe[0] == cat_name and recipe[2] == owner :
                render_recipe.append(recipe)
        return render_recipe
