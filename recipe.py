import re
regex_category = "[a-zA-Z0-9- .]+$"
class Recipe(object):
    """
      Users Class to handle methods to do with recipes categories and actual recipes
      """
    recipe_categories = {}
    def __init__(self, cat_name=None, owner=None):
        """ Initializing  class instance variables"""
        self.cat_name = cat_name
        self.owner = owner

    def category_register(self, cat_name,owner):
        """ method that defines the elements required to create an account """
        if re.match(regex_category, cat_name):
            if cat_name != '' and cat_name.strip():
                if cat_name not in self.recipe_categories :
                    self.recipe_categories[cat_name] = {"cat_name":cat_name,"owner":owner,}
                    return "200,OK"
                return "204,Category exists"
            return "205,Invalid Name"
        return "205,Regex mismatch"

