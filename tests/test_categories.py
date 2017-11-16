"""Class to category creation, editing, category routes and category deletion"""
import unittest
from models.user import Users
from models.categories import Categories
from app import app


class CategoryTest(unittest.TestCase, Users):
    """ Class performing unit testing for class Recipe"""

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newCat = Categories()
        self.newCat.category_register("category", "waweru@gmail.com")
        self.newCat.category_edit(
            "category", "category_one", "waweru@gmail.com")
        app.config['TESTING'] = True
        self.test_app = app.test_client()

    def test_category_register_route(self):
        """ Test to check if category register route works"""
        response = self.test_app.get('/cat_register')
        self.assertEqual(response.status_code, 200)

    def test_view_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/view_category/Lunch')
        self.assertEqual(response.status_code, 200)

    def test_category_registration(self):
        """ Test to check succesful category creation"""
        category_registration = self.newCat.category_register(
            "category_one", "waweruh@gmail.com")
        self.assertEqual("Successfully created category",
                         category_registration)
    def test_category_exists(self):
        """ Test to check if category_name exists """
        category_exists = self.newCat.category_register(
            "category", "waweru@gmail.com")
        self.assertEqual("Category exists", category_exists)

    def test_null_category(self):
        """ Test to test creation of a null category name"""
        category_registration = self.newCat.category_register(
            "", "waweru@gmail.com")
        self.assertEqual("Category name is null", category_registration)

    def test_edit_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/category_edit/Lunch')
        self.assertEqual(response.status_code, 200)

    def test_delete_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/category_delete')
        self.assertEqual(response.status_code, 200)

    def test_invalid_category_name(self):
        """Test to check if category_name follows the one specified by regex"""
        category_registration = self.newCat.category_register(
            "&#*", "waweru@gmail.com")
        self.assertEqual("category name has special characters",
                         category_registration)

    def test_update_category_regex(self):
        """ Test for category name regex pattern name on update  """
        category_check_regex = self.newCat.category_edit(
            "category_one", "@@@", "mwaz")
        self.assertIn("category name has special characters",
                      category_check_regex)

    def test_update_category_exists(self):
        """ Test for invalid  category name on update  """
        category_exists = self.newCat.category_edit(
            "categoryone", "category", "mwaz")
        self.assertEqual("category name exists", category_exists)
