# from flask import url_for
# from flask_testing import TestCase
# import requests_mock

# from app import app
# import pytest
# import urllib3
# from flask import Flask, render_template, request
# import os
# from flask_sqlalchemy import SQLAlchemy

# def test_homepage():
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'http://teams_api:5001/get_teams')
#     assert 200 == r.status

# class TestBase(TestCase):
#     def create_app(self):
#         return app

# class TestResponse(TestBase):
#     def test_home(self):
#         with requests_mock.Mocker() as m:
#             m.get('http://teams_api:5001/get_teams', team1='LA Lakers', team2='Toronto Raptors')
#             m.get('http://stadium_api:5002/get_stadium', stadium='Staples Center')
#             m.post('http://chance_api:5003/get_chance', chance=85)
#             response = self.client.get(url_for('home'))
# #             self.assertEqual(response.status_code, 200)
#             self.assertIn(b'LA Lakers vs Toronto Raptors', response.data)