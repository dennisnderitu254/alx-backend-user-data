#!/usr/bin/env python3
""" Session Authentication """

from api.v1.auth.auth import Auth
from typing import TypeVar
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    Session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a user_id
        """
        if not user_id or type(user_id) != str:
            return
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[user_id] = session_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if not session_id or type(session_id) != str:
            return
        return SessionAuth.user_id_by_session_id.get(session_id, None)

    # def current_user(self, request=None):
    #     """
    #     Current user
    #     """
    #     session_cookie = self.session_cookie(request)
    #     user_id = self.user_id_for_session_id(session_cookie)
    #     return User.get(user_id)

    # def destroy_session(self, request=None):
    #     """
    #     Destroy session
    #     """
    #     if request is None:
    #         return False
    #     session_cookie = self.session_cookie(request)
    #     if session_cookie is None:
    #         return False
    #     user_id = self.user_id_for_session_id(session_cookie)
    #     if user_id is None:
    #         return False
    #     del self.user_id_by_session_id[session_cookie]
    #     return True
