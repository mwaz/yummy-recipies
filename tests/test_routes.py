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
