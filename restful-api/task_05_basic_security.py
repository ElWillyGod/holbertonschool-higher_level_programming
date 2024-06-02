#!/usr/bin/python3
"""seguridad de apis"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, jwt_required,
                                create_access_token,
                                get_jwt_identity)


users = {
      "user1": {"username": "user1",
                "password": generate_password_hash("password"),
                "role": "user"},
      "admin1": {"username": "admin1",
                 "password": generate_password_hash("password"),
                 "role": "admin"}
      }


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_Key_Here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


@app.route("/basic-protected") 
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route("/login", methods=["POST"])
def login():
    user = request.get_json()
    username = user.get('username')
    password = user.get('password')
    userAcces = users.get(username)

    if userAcces and check_password_hash(user['password'], password):

        access_token = create_access_token(
                identity={'username': username, 'role': user['role']})

        return jsonify(access_token=access_token)

    return jsonify({'error': "data invalid"}), 401


@app.route("/jwt-protected")
@jwt_required()
def protected_route():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_user():

    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return "Admin Access: Granted"

    return jsonify({'error': "no es un admin"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
