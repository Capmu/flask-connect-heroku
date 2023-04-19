from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()
USER_DATA = {
    "admin": "1234"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


@app.route('/')
def home():
    return "Flask heroku app."

@app.route('/private')
@auth.login_required
def private():
    return "Flask heroku app. (private)"


if __name__ == '__main__':
    app.run()