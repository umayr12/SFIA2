from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

# class TestResponse(TestBase):
#     def test_home(self):
#         with requests_mock.Mocker() as m:
#             m.get('http://teams_api:5001/get_teams', team1='LA Lakers', team2='Toronto Raptors')
#             # m.post('http://stadium_api:5002/get_stadium', stadium='Staples Center')
#             response = self.client.get(url_for('home'))
#             self.assertEqual(response.status_code, 200)
#             self.assertIn(b'LA Lakers vs Toronto Raptors', response.data)