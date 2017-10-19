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

 