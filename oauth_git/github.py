"""
https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/
https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
"""

import requests
from flask import Flask, redirect, url_for, escape, request
import re

app = Flask(__name__)

CLIENT_ID = "..."
CLIENT_SECRET = "..."
AUTH_URL = "https://github.com/login/oauth/authorize"
REDIRECT_URI = "http://localhost:5000/redirect/"


app = Flask(__name__)


@app.route('/')
def login():
    """1. Request a user's GitHub identity"""
    url = AUTH_URL + f"?client_id={CLIENT_ID}&login=krother&redirect_uri={REDIRECT_URI}"
    return redirect(url)


@app.route('/redirect/')
def redirect_from_github():
    """2. Users are redirected back to your site by GitHub"""
    params = {'client_id': CLIENT_ID,
              'client_secret': CLIENT_SECRET,
              'code': request.args['code'],
              }
    r = requests.post("https://github.com/login/oauth/access_token", params)
    if r.status_code == 200:
        print(r.text)
        access_token = re.findall('access_token\=([^\&]+)', r.text)[0]
        print(access_token)
        #
        # now do stuff with access token
        #
        return redirect(url_for('goal'))
    return redirect(url_for('fail'))


@app.route('/goal')
def goal():
    return "DONE!!!"

@app.route('/fail')
def fail():
    return "*** FAIL ***"
