#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {"jane": {"username": "jane",
                  "name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    if "username" in data:
        if data["username"] in users:
           pass 
        users[data["username"]] = data
        return jsonify(data), 201


if __name__ == "__main__":
    app.run()
