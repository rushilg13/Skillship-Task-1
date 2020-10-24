from flask import Flask, render_template, url_for, request, jsonify
import requests
from flask_jwt import JWT, jwt_required, current_identity, jwt

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/register', methods=['POST', 'GET'])
def home():
    return render_template("home.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    email = request.form['email']
    password = request.form['password']
    encoded_pwd = jwt.encode({'password':password}, 'secret', algorithm='HS256')
    print(encoded_pwd)
    print(email)
    return ("logged in")

@app.route('/api', methods=['GET'])
def api():
    return "Hi"

if __name__ == "__main__":
    app.run(debug=True)