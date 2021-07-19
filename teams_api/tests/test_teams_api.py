# from unittest.mock import patch
# from flask import url_for
# from flask_testing import TestCase

# from app import app

# class TestBase(TestCase):
#     def create_app(self):
#         return app

# class TestAnimalApi(TestBase):
#     def test_get_animal(self):
#         for num in range(20):
#             response = self.client.get(url_for('get_teams'))
#             self.assertIn(response.data.decode("utf-8"),['LA Lakers', 'Toronto Raptors', 'Brooklyn Nets'])
