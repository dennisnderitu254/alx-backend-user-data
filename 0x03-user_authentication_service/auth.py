#!/usr/bin/env python3
"""
hash password
"""

from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import TypeVar


def _hash_password(password: str) -> str:
    """
    _hash_password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    _generate_uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """
        valid login
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        create_session
        """
        try:
            user = self._db.find_user_by(email=email)
            sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=sess_id)
            return sess_id
        except NoResultFound:
            return

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        get_user_from_session_id
        """
        if session_id is None:
            return
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except NoResultFound:
            return

# # Test the _hash_password method
# if __name__ == "__main__":
#     password = "Hello Holberton"
#     hashed_password = _hash_password(password)
#     print(hashed_password)
