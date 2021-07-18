from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app
import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('POST', 'http://chance_api:5003/get_chance')
    assert 200 == r.status