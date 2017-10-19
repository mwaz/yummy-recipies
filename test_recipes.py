import unittest
from unittest import TestCase
from recipes import Recipe


class RecipeTest(unittest.TestCase):
    """
       Class performing unit testing for class Recipe
    """

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.recipes = Recipe()
        self.recipes.Recipes = {}

    def test_for_creating_a_recipe_category(self):
        """  method definition to test for Creating a recipe category """
        output = self.recipes.create('recipe_category', 'waweru@gmail.com')
        self.assertEqual(4, output, "Recipe category successfully created")

    def test_if_recipes_name_is_empty(self):
        """ method definition to test for adding a recipe with an empty title """
        output = self.recipes.create('', 'recipe_category_owner')
        self.assertEqual(4, output, "please fill all fields")

   