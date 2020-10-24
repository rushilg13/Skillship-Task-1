from flask import Flask, render_template
import requests
import json
import asyncio

app = Flask(__name__)

url = '''fetch('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => response.json())
        .then(json => console.log(json))'''

response = requests.get("https://jsonplaceholder.typicode.com/todos/1/posts")
todos = json.loads(response.text)
@app.route('/')

def home():
    task1 = todos[1]
    return render_template("home.html", task1=task1)    

if __name__ == "__main__":
    app.run(debug=True)