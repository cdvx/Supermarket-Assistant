from datetime import datetime, timedelta

from flask import (Flask, Response, flash, json, jsonify, redirect, request,
                   url_for)
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'wiiu392#$%#&&B^^R@!FVDU@!*125e5'
jwt = JWTManager(app)



@app.route('api/v1/auth/login', methods=['POST'])
def login():
    if not request.is_json:
            return jsonify({'message': 'JSON missing in request!'}), 400

    username = request.args.get('username', None)
    password = request.args.get('password', None)
    user_role = request.args.get('role', None)
    if not username:
        return jsonify({
            'message': 'Required parameter: username missing!'
        }), 400
    elif not password:
        return jsonify({
            'message': 'Required parameter: password missing!'
        }), 400
    elif not user_role:
        return jsonify({
            'message': 'Required parameter: user_role missing!'
        }), 400

    user = [user for user in users if user['username']
            == username and user['password'] == password
            and user_role == user['role']]
    if not user:
        return jsonify({'message': 'Invalid username, password orz role'}), 401

    access_token = create_access_token(
        identity=username,
        fresh=timedelta(minutes=30)
    )
    msg = {'access_token': f'{access_token}'}

    return jsonify({f'access token created for user {username}': msg}), 200

@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({'message': 'JSON missing in request!'}), 400

    username = request.args.get('username', None)
    user_role = request.args.get('role', None)
    password = request.args.get('password', None)
    repeat_password = request.args.get('repeat_password', None)

    if not username:
        return jsonify({
            'message': 'Required parameter: username missing!'
        }), 400
    elif not user_role:
        return jsonify({'message': 'Required parameter: user_role missing!'}), 400
    elif not password:
        return jsonify({'message': 'Required parameter: email missing!'}), 400
    else:
        if not repeat_password:
            msg = 'Required parameter: repeat_password missing!'
            return jsonify({'message': f'{msg}'}), 400

    if valid_user(username, user_role):

        if repeat_password == password:

            user = {
                'username': username,
                'role': user_role
                'email': email,
                'password': password,
            }
            user = User(user_role, username, password)
            users.append(user)
            return jsonify({
                'success': f"{username}'s account created succesfully"
            }), 200

        return jsonify({
            'message': 'Password does not match repeat_password'
        }), 401
    return jsonify({'message': f'username {username} already taken!'}), 401


def valid_user(username, user_role):
    for user in users:
        if user_role.lower() in ['owner', 'store managers', 'till attendants']:
            existing_user = [[user['username'], user['role']]
                             for user in users if user['username'] == username]
        if not existing_user:
            return True
    return False
