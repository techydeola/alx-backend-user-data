#!/usr/bin/env python3
""" a module for handling authentication
"""

from flask import request
from typing import List, TypeVar


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

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object method
        """

        return None
