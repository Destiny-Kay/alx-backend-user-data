#!/usr/bin/env python3
'''Encrypting password'''
import bcrypt


def hash_password(password: str) -> str:
    '''Hashes a password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Validates a password'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
