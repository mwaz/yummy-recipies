import re
import random
recipe_categories = {}


class Recipe(object):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
      """

    def __init__(self, cat_name=None, cat_id=None, owner=None):
        """ Initializing  class instance variables"""
        self.cat_name = cat_name
        self.cat_id = cat_id
        self.owner = owner

    def category_register(self, cat_name, cat_id, owner):
        """ method that defines the elements required to create an account """
        reg_category = "[a-zA-Z0-9- .]+$"
        if re.match(reg_category, cat_name):
            if reg_category != '' :
                if reg_category not in recipe_categories.keys():
                    if cat_id not in recipe_categories.keys():
                        recipe_categories[cat_id] = {'cat_name': cat_name,
                                                    'cat_id': cat_id,
                                                    'owner' : owner,
                                                    }
                        return 1
                    return 2
                return 3
            return 4
        return 5
