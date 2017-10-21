import unittest
from recipe import Recipe


class RecipeTest(unittest.TestCase):
    """ Class performing unit testing for class Recipe"""
    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newCat= Recipe()

    def test_category_registration(self):
        """ Test to test function create category """
        self.newCat.recipe_categories = {}
        self.newCat.category_register("category_one", "waweru@gmail.com")
        category_registration = self.newCat.category_register("category", "waweru@gmail.com")
        self.assertEqual("200,OK", category_registration, " success in creating category")

    def test_category_exists(self):
        """ Test to check if category_name exists """
        self.newCat.recipe_categories = {}
        self.newCat.category_register("category", "waweru@gmail.com")
        category_registration = self.newCat.category_register("category", "waweru@gmail.com")
        self.assertEqual("204,Category exists", category_registration, "category name already exists")

    def test_empty_category(self):
        """ Test to check empty category name """
        category_empty = self.newCat.category_register("", "waweru@gmail.com")
        self.assertEqual("205,Regex mismatch", category_empty, "category name is null")

    def test_null_category(self):
        """ Test to test creation of a null category name"""
        category_registration = self.newCat.category_register(" ", "waweru@gmail.com")
        self.assertEqual("205,Invalid Name", category_registration, "category name is empty")

 