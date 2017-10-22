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
