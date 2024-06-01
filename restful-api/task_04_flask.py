#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from requests import request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(users)


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    users[username] = data
    return f"User {username} added successfully!", 201


if __name__ == "__main__":
    app.run()
