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
    
#     def test_get_noise(self):
#         test_cases=[("cow","moo"), ("pig","oink"), ("horse", "neigh")]
#         for case in test_cases:
#             response = self.client.post(url_for('get_noise'), data=case[0])
#             self.assertEqual(response.data.decode("utf-8"),case[1])
