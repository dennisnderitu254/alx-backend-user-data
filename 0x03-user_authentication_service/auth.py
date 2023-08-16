#!/usr/bin/env python3
"""
hash password
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    _hash_password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# # Test the _hash_password method
# if __name__ == "__main__":
#     password = "Hello Holberton"
#     hashed_password = _hash_password(password)
#     print(hashed_password)
