#!/usr/bin/env python3
'''Module for api authentication'''
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    '''Auth class template'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''checks whether urls require authentication'''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        '''authorization_header'''
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''return None'''
        return None

    def session_cookie(self, request=None):
        '''returns a cookie value from a request'''
        if request is None:
            return None
        cookie_name = getenv("SESSION_NAME")
        session_id = request.cookies.get(cookie_name)
        return session_id