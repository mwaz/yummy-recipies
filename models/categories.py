import re

from models.user import Users
from models.recipe import Recipe


#class Recipe inherits from the User class, where every method present
#in the Users class can be used in the Recipes class 

class Categories(Users):
    """
      Categories Class to handle methods to do with recipes categories
    """

    def __init__(self, cat_name=None, owner=None):
        """ Initializing Category class instance variables"""
        self.cat_name = cat_name
        self.owner = owner
        self.regex_name = "[a-zA-Z- .]+$"
        self.recipe_categories = []
        self.new_recipe = Recipe() 

    def category_register(self, cat_name, owner):
        """ method that defines the elements required to create an account """
    
        if cat_name:
            cat_name = re.sub(r'\s+', ' ', cat_name).strip()

        cat_name = None if cat_name == " " else cat_name.title()

        if not(cat_name):
            return "Category name is null"
            
        if not re.search(self.regex_name, cat_name):
            return "category name has special characters"
            
        if (any(cat_name == category_list[0] and owner == category_list[1]
                for category_list in self.recipe_categories)) == True:
            return "Category exists"
            
        self.recipe_categories.append([cat_name, owner, ])
        return "Successfully created category"

    def category_edit(self, cat_name, new_cat_name, owner):
        """ method that defines the elements required to edit a category """
        if new_cat_name:
            new_cat_name = re.sub(r'\s+', ' ', new_cat_name).strip()
 
        new_cat_name = None if new_cat_name == " " else new_cat_name

        if not(new_cat_name):
            return "Null category name"

        if not re.search(self.regex_name, new_cat_name):
            return "category name has special characters"

        for category_list in self.recipe_categories:
            #The loop returns all the categories that belong to a 
            #specific ower and only updates when te category name
            #exists in the list
        
            if category_list[0] == cat_name and category_list[1] == owner:
                category_list[0] = new_cat_name

                for recipe_list in self.new_recipe.recipes:
                    recipe_index = new_recipe.recipes.index(recipe_list)
                    self.new_recipe.recipes[recipe_index][0] = new_cat_name
                return "successfully updated category name"
        return "category name exists"
                       

    def category_delete(self, cat_name, owner):
        
        #method that defines the elements required delete a category 
        #the for loop loops to check if the category name exists and 
        #in recipe_categories list then deletes the index of that 
        #category.

        for category_list in self.recipe_categories:
            if category_list[0] == cat_name and category_list[1] == owner:
                category_index = self.recipe_categories.index(category_list)
                self.recipe_categories.pop(category_index)
                
                return "successfully deleted category"
        return "Category doesnt exist"

              
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
