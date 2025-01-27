from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

user = 'doctor'
password_hash = generate_password_hash(os.getenv('RAS_HEALTH_PASSWORD'))

@auth.verify_password
def verify_credentials(credential_username, credential_password):
    if credential_username == user and check_password_hash(password_hash, credential_password):
        return credential_username

@app.post('/')
@auth.login_required
def health():
    con = sqlite3.connect(os.getenv('RAS_HEALTH_DB'))
    with con:
        con.execute('INSERT INTO ras_health_log (ras_timestamp) VALUES (?);', (request.get_json()['ras_timestamp'],))
    con.close()
    return 'ok'
