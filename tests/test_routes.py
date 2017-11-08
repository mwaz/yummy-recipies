import unittest

from app import app


class TestUsers(unittest.TestCase):
    """
    class to test the class user
    """

    def setUp(self):
        """ Method called to prepare the test fixture """

        app.config['TESTING'] = True
        self.test_app = app.test_client()

    def test_root_route(self):
        """ test to see that homepage loads"""
        response = self.test_app.get('/')
        self.assertIn(b'Index', response.data)


    def test_login_route(self):
        """ Test to check if the login route loads"""
        response = self.test_app.get('/login')
        self.assertEquals(response.status_code, 200)

    def test_register_route(self):
        """ Test to check if the user register route loads"""
        response = self.test_app.get('/register')
        self.assertEquals(response.status_code, 200)

    def test_category_register_route(self):
        """ Test to check if category register route works"""
        response = self.test_app.get('/cat_register')
        self.assertEquals(response.status_code, 200)

    def test_view_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/view_category/Lunch')
        self.assertEquals(response.status_code, 200)

    def test_edit_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/category_edit/Lunch')
        self.assertEquals(response.status_code, 200)

    def test_delete_category_route(self):
        """ Test to check if view category route works"""
        response = self.test_app.get('/category_delete')
        self.assertEquals(response.status_code, 200)

    def test_recipe_register_route(self):
        """ Test to check if recipe register route works"""
        response = self.test_app.get('/recipe_register')
        self.assertEquals(response.status_code, 200)

    def test_recipe_edit_route(self):
        """ Test to check if recipe edit route works"""
        response = self.test_app.get('/recipe_edit/Panckakes')
        self.assertEquals(response.status_code, 200)

    def test_recipe_delete_route(self):
        """ Test to check if recipe delete route works"""
        response = self.test_app.get('/recipe_delete')
        self.assertEquals(response.status_code, 200)
