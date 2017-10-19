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

   
