import unittest
from models.user import Users
from models.recipe import Recipe
from models.categories import Categories


class RecipeTest(unittest.TestCase, Categories):
    """ Class performing unit testing for class Recipe"""

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newRecipe = Recipe()
        self.newCategory = Categories()
        self.recipe_register = self.newRecipe.recipe_register(
            "category", "recipe", "waweru@gmail.com", "recipe_ingredients", "recipe_methods")
        self.newCategory.category_register("category_one", "waweru@gmail.com")

    def test_recipe_registration(self):
        """ Test for method create recipe """
        recipe_success_registration = self.newRecipe.recipe_register(
            "category_one", "recipee", "waweru@gmail.com", "recipe_ingredients", "recipe_methods")
        self.assertEqual("successfully created recipe",
                         recipe_success_registration)

    def test_recipe_regex_match(self):
        """ Test for recipe name regex match """
        recipe_name_regex_format = self.newRecipe.recipe_register(
            "category", "@@@", "waweru@gmail.com", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Recipe name has special characters",
                         recipe_name_regex_format)

    def test_recipe_null_name(self):
        """ Test for null recipe name  """
        recipe_null_name = self.newRecipe.recipe_register(
            "category", "", "waweru@gmail.com", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Null recipe name", recipe_null_name)

    def test_recipe_null_ingredients(self):
        """ Test for null recipe ingredients """
        recipe_null_ingredients = self.newRecipe.recipe_register(
            "category", "recipe_name", "waweru@gmail.com", "", "recipe_methods")
        self.assertEqual("Null recipe ingredients", recipe_null_ingredients)

    def test_recipe_null_methods(self):
        """ Test for null recipe preparation methods  """
        recipe_null_methods = self.newRecipe.recipe_register(
            "category", "recipe_name", "waweru@gmail.com", "recipe_ingredients", "")
        self.assertEqual("Null recipe method", recipe_null_methods)

    def test_recipe_exists(self):
        """ Test for method if recipe exists """
        recipe_exists = self.newRecipe.recipe_register(
            "category", "recipe", "waweru@gmail.com", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Recipe exists", recipe_exists)

    def test_edit_recipe_regex_format(self):
        """ Test for recipe name regex pattern name on update  """
        edit_recipe_regex = self.newRecipe.recipe_edit(
            "@@@", "recipe_name", "category_one", "mwaz", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Recipe name has special characters",
                         edit_recipe_regex)

    def test_edit_recipe_is_null(self):
        """ Test for null recipe name on update  """
        recipe_edit_is_null = self.newRecipe.recipe_edit(
            "", "categoryone", "recipe_name", "mwaz", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Null recipe name", recipe_edit_is_null)

    def succss_recipe_name_edit(self):
        """ Test for successful recipe name on update  """
        recipe_edit_success = self.newRecipe.recipe_edit(
            "new_recipe", "categoryone", "recipe_name", "mwaz", "recipe_ingredients", "recipe_methods")
        self.assertEqual("Successfully edited recipe", recipe_edit_success)
