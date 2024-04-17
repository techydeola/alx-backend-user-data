#!/usr/bin/env python3
""" a module for handling authentication
"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """A class for authentication

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A public method
            Returns: False
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if (f"{path}" + "/") in excluded_paths:
            return False
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

        return False

    def authorization_header(self, request=None) -> str:
        """ A public method
            Returns: None
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object method
        """

        return None

    def session_cookie(self, request=None):
        """ returns a cookie value froma request
        """
        if request is None:
            return None
        session_name = os.environ.get('SESSION_NAME')

        return request.cookies.get(session_name)
