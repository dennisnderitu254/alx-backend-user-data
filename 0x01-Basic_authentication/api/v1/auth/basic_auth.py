#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """
    class BasicAuth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        return the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        header_array = authorization_header.split(" ")
        if header_array[0] != "Basic":
            return None
        else:
            return header_array[1]
        # if (authorization_header is None or
        #         not isinstance(authorization_header, str) or
        #         not authorization_header.startswith("Basic")):
        #     return None

        # return authorization_header[6:]
