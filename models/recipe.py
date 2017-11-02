import re

from models.user import Users

#class Recipe inherits from the User class, where every method present
#in the Users class can be used in the Recipes class 

class Recipe(Users):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
    """
    #list to store recipe categories 
    recipe_categories = []
    #list to store recipes
    recipes = []

    def __init__(self, cat_name=None, owner=None, recipe_name=None):
        """ Initializing Recipe class instance variables"""
        self.cat_name = cat_name
        self.owner = owner
        self.recipe_name = recipe_name
        self.regex_name = "[a-zA-Z0-9- .]+$"

    def category_register(self, cat_name, owner):
        """ method that defines the elements required to create an account """
    
        if not(cat_name):
            return "205,Invalid Name"
            #returns status code 205 and routes it to the view

        if not re.search(self.regex_name, cat_name):
            return "205,Regex mismatch"
            #returns status code 205 and routes it to the view

        if self.recipe_categories == []:
            self.recipe_categories.append(
                [cat_name, owner, ])
            return "200,OK"
            #returns status code 200 and routes it to the view

        if (any(cat_name == category_list[0] and owner == category_list[1]
                for category_list in self.recipe_categories)) == True:
            return "204,Category exists"
            #returns status code 204 and routes it to the view

        self.recipe_categories.append([cat_name, owner, ])
        return "200,OK"

    def category_edit(self, cat_name, new_cat_name, owner):
        """ method that defines the elements required to edit a category """
        if new_cat_name:
            new_cat_name = re.sub(r'\s+', ' ', new_cat_name).strip()

        new_cat_name = None if new_cat_name == " " else new_cat_name

        if not(new_cat_name):
            return "205,Invalid Name"

        if not re.search(self.regex_name, new_cat_name):
            return "205,Regex mismatch"

        for category_list in self.recipe_categories:
            #The loop returns all the categories that belong to a 
            #specific ower and only updates when te category name
            #exists in the list
        
            if category_list[0] == cat_name and category_list[1] == owner:
                category_list[0] = new_cat_name

                for recipe_list in self.recipes:
                    recipe_index = self.recipes.index(recipe_list)
                    self.recipes[recipe_index][0] = new_cat_name
                return "200,OK"
                return "200,OK,UPDATE"
                #status code to show successful update

    def category_delete(self, cat_name, owner):
        
        #method that defines the elements required delete a category 
        #the for loop loops to check if the category name exists and 
        #in recipe_categories list then deletes the index of that 
        #category.
        
        for category_list in self.recipe_categories:
            if category_list[0] == cat_name and category_list[1] == owner:
                category_index = self.recipe_categories.index(category_list)
                self.recipe_categories.pop(category_index)
                return "200,OK"

    def recipe_register(self, cat_name, recipe_name, owner):
        """ method that defines the elements required to create an account """
        if recipe_name:
            recipe_name = re.sub(r'\s+', ' ', recipe_name).strip()

        recipe_name = None if recipe_name == " " else recipe_name

        if not (recipe_name):
            return "205,Invalid Name"

        if not re.search(self.regex_name, recipe_name):
            return "205,Regex mismatch"

        if self.recipes == []:
            #checks if the recipes list is empty
            #if that is the case, the loop for checking
            #if recipe is present in the list will not take place
            self.recipes.append(
                [cat_name, recipe_name, owner])
            return "200,OK"

        if (any(recipe_name == recipe_list[1]
                and owner == recipe_list[2]
                and cat_name == recipe_list[0]
                for recipe_list in self.recipes)) == True:
            #returns an error if the recipe name is in the same category
            #and having the same owner 

            return "204,Recipe exists"

        #if the recipe name meets the condition it is added to the recipes list
        self.recipes.append([cat_name, recipe_name, owner, ])
        return "200,OK"

    def recipe_edit(self, new_recipe_name, recipe_name, cat_name, owner):
        """ method that defines how to edit a recipe, the method takes 
            the new recipe name as a parameter, the recipe name and the category
            name, all belonging to the logged in user
        """
        if new_recipe_name:
            new_recipe_name = re.sub(r'\s+', ' ', new_recipe_name).strip()

        new_recipe_name = None if new_recipe_name == " " else new_recipe_name
        
        if not (new_recipe_name):
            return "205,Invalid Name"

        if not re.search(self.regex_name, new_recipe_name):
            return "205,Regex mismatch"

        for recipe_list in self.recipes:

            #checks to find if the new recipe name exists in the recipes list
            if (any(new_recipe_name == recipe_list[1] for
                    recipe_list in self.recipes)) == True:

                return "204,Recipe exists"

        recipe_list[1] = new_recipe_name
        return "200,OK"

    def recipe_delete(self, recipe_name, cat_name, owner):
        """ method that defines the elements required to delete a recipe """
        for recipe_list in self.recipes:
            if recipe_list[1] == recipe_name and recipe_list[0] == cat_name and owner:
                recipe_index = self.recipes.index(recipe_list)
                del self.recipes[recipe_index]
                return "200,OK"

    def view_recipe_category(self, owner):
        """
        method used to display all the categories that are present in 
            a users recipe_category list
        """
        category_data = self.recipe_categories
        render_category_data = []
        for category in category_data:
            if category[1] == owner:
                render_category_data.append(category)
        return render_category_data

    def view_recipe(self, cat_name, owner):
        """
        method to view all the recipes that belong to a category 
        with the same owner
         """
        recipe_data = self.recipes
        render_recipe_data = []
        for recipe in recipe_data:
            if recipe[0] == cat_name and recipe[2] == owner:
                render_recipe_data.append(recipe)
        return render_recipe_data
