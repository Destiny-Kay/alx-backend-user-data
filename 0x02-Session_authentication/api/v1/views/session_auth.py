#!/usr/bin/env python3
'''session views module'''
from api.v1.views import app_views
from flask import jsonify, request, abort
from typing import Tuple
from models.user import User
import os


@app_views.route('/auth_session/login', strict_slashes=False, methods=['POST'])
def login() -> Tuple[str, int]:
    '''handles all routes for session authentication'''
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password.strip()) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(getattr(users[0], 'id'))
    res = jsonify(users[0].to_json())
    res.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return res


@app_views.route('/api/v1/auth_session/logout',
                 strict_slashes=False, methods=['DELETE'])
def logout():
    '''logout view'''
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})
