import unittest
from recipe import Recipe


class RecipeTest(unittest.TestCase):
    """ Class performing unit testing for class Recipe"""
    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newCat = Recipe()

    def test_category_registration(self):
        """ Test to test function create category """
        self.newCat.recipe_categories = {}
        self.newCat.category_register("category_one", "waweru@gmail.com")
        category_registration = self.newCat.category_register("category", "waweru@gmail.com")
        self.assertIn("200,OK", category_registration, "200,OK")

    def test_category_exists(self):
        """ Test to check if category_name exists """
        self.newCat.recipe_categories = {}
        self.newCat.category_register("category", "waweru@gmail.com")
        category_registration = self.newCat.category_register("category", "waweru@gmail.com")
        self.assertIn("204,Category exists", category_registration, "204,Category exists")

    def test_empty_category(self):
        """ Test to check empty category name """
        category_empty = self.newCat.category_register("", "waweru@gmail.com")
        self.assertIn("205,Regex mismatch", category_empty, "205,Regex mismatch")

    def test_null_category(self):
        """ Test to test creation of a null category name"""
        category_registration = self.newCat.category_register(" ", "waweru@gmail.com")
        self.assertIn("205,Invalid Name", category_registration, "205,Invalid Name")

    def test_invalid_category_name(self):
        """Test to check if category_name follows the one specified by regex"""
        category_registration = self.newCat.category_register("&#*", "waweru@gmail.com")
        self.assertIn("205,Regex mismatch", category_registration, "205,Regex mismatch")


    def test_recipe_registration(self):
        """ Test for method create recipe """
        self.newCat.recipe = {}
        self.newCat.recipe_register("category_one", "recipe1", "waweru@gmail.com")
        recipe_registration = self.newCat.recipe_register("category", "recipe2" , "waweru@gmail.com")
        self.assertIn("200,OK", recipe_registration, "200,OK")

    def test_recipe_regex_match(self):
        """ Test for recipe name regex match """
        recipe_registration = self.newCat.recipe_register("categor@y", "recipe1", "waweru@gmail.com")
        self.assertIn("205,Regex mismatch", recipe_registration, "205,Regex mismatch")

    def test_recipe_empty_name(self):
        """ Test for empty recipe name  """
        recipe_null = self.newCat.recipe_register(" ", "recipe1", "waweru@gmail.com")
        self.assertIn("205,Invalid Name", recipe_null, "205,Invalid Name")

    def test_recipe_null_name(self):
        """ Test for null recipe name  """
        recipe_null = self.newCat.recipe_register(' ', "recipe", "waweru@gmail.com")
        self.assertIn("205,Invalid Name", recipe_null, "205,Invalid Name")

    def test_recipe_exists(self):
        """ Test for method if recipe exists """
        self.newCat.recipe = {}
        self.newCat.recipe_register("category", "recipe1", "waweru@gmail.com")
        recipe_registration = self.newCat.recipe_register("category", "recipe1", "waweru@gmail.com")
        self.assertIn("204,Recipe exists", recipe_registration, "204,Recipe exists")






