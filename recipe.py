import re


class Recipe(object):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
      """
    recipe_categories = {}
    def __init__(self, cat_name=None, cat_id=None, owner=None):
        """ Initializing  class instance variables"""
        self.cat_name = cat_name
        self.cat_id = cat_id
        self.owner = owner

    def category_register(self, cat_name,owner):
        """ method that defines the elements required to create an account """
        reg_category = "[a-zA-Z0-9- .]+$"
        if re.match(reg_category, cat_name):
            if cat_name != '' and cat_name != ' ':
                if cat_name not in self.recipe_categories :
                    self.recipe_categories[cat_name] = {"cat_name":cat_name,"owner":owner,}
                    return 1
                return 2
            return 3

