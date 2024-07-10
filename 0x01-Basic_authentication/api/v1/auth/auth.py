#!/usr/bin/env python3
'''Module for api authentication'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''Auth class template'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''checks whether urls require authentication'''
        return False

    def authorization_header(self, request=None) -> str:
        '''authorization_header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''return None'''
        return None
