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
        if not(cat_name):
            return "205,Invalid Name"

        if not re.search(regex_name, cat_name):
            return "205,Regex mismatch"

        if self.recipe_categories == []:
            self.recipe_categories.append([cat_name.replace(" ", "_"), owner, ])
            return "200,OK"
            
        if (any(cat_name == category_list[0] and owner == category_list[1]
            for category_list in self.recipe_categories)) == True:
            return "204,Category exists"

        self.recipe_categories.append([cat_name.replace(" ", "_"), owner,])
        return "200,OK"


    def category_edit(self, cat_name, new_cat_name, owner):
        """ method that defines the elements required delete a category """
        if not(cat_name):
            return "205,Invalid Name"

        if not re.search(regex_name, new_cat_name):
            return "205,Regex mismatch"

        for category_list in self.recipe_categories:
            if category_list[0] == cat_name and category_list[1] == owner:
                category_list[0] = new_cat_name.replace(" ", "_")

                for recipe_list in self.recipes:
                    recipe_index = self.recipes.index(recipe_list)
                    self.recipes[recipe_index][0] = new_cat_name.replace(" ", "_")
                return "200,OK"
                return "200,OK,UPDATE"
            
        # for recipe_list in self.recipes:
        #     recipe_index = self.recipes.index(recipe_list)
        #     self.recipes[recipe_index][0] = new_cat_name.replace(" ", "_")
        #     return "200,OK"


    def category_delete(self, cat_name, owner):
        """ method that defines the elements required delete a category """
        for category_list in self.recipe_categories:
            if category_list[0] == cat_name and category_list[1] == owner:
                category_index = self.recipe_categories.index(category_list)
                self.recipe_categories.pop(category_index)
                return "200,OK"
          

    def recipe_register(self, cat_name, recipe_name, owner):
        """ method that defines the elements required to create an account """
        if not (recipe_name):
            return "205,Invalid Name"

        if not re.search(regex_name, recipe_name):
            return "205,Regex mismatch"

        if self.recipes == []:
            self.recipes.append([cat_name, recipe_name.replace(" ", "_"), owner])
            return "200,OK"

        if (any(recipe_name == recipe_list[1] 
            and owner == recipe_list[2] 
            and cat_name == recipe_list[0] 
            for recipe_list in self.recipes)) == True:
            return "204,Recipe exists"

        self.recipes.append([cat_name, recipe_name.replace(" ", "_"), owner, ])
        return "200,OK"

    def recipe_edit(self, new_recipe_name, recipe_name, cat_name, owner):
        """ method that defines the elements required to edit a recipe"""
        if not (new_recipe_name):
            return "205,Invalid Name"

        if not re.search(regex_name, new_recipe_name):
            return "205,Regex mismatch"

        for recipe_list in self.recipes:
           
            # if (any(new_recipe_name == recipe_list[1] for
            #  recipe_list in self.recipes)) == True:
            #     return "204,Recipe exists"
            
            print (recipe_list[1] + "THIS IS RECIPE LIST")
            print (recipe_name + "THIS IS RECIPE NAME")
            if recipe_list[1]==recipe_name:
                recipe_list[1] = new_recipe_name.replace(" ", "_")
                return "200,OK"


    def recipe_delete(self, recipe_name, cat_name, owner):
        """ method that defines the elements required to delete a recipe """
        for recipe_list in self.recipes:
            if recipe_list[1] == recipe_name and recipe_list[0] == cat_name and owner :
                recipe_index = self.recipes.index(recipe_list)
                del self.recipes[recipe_index]
                return "200,OK"

    def view_recipe_category(self, owner):
        category_data = self.recipe_categories
        render_category_data = []
        for category in category_data:
            if category[1] == owner:
                render_category_data.append(category)
        return render_category_data

    def view_recipe(self, cat_name, owner):
        recipe_data = self.recipes
        render_recipe_data = []
        for recipe in recipe_data:
            if recipe[0] == cat_name and recipe[2] == owner :
                render_recipe_data.append(recipe)
        return render_recipe_data
