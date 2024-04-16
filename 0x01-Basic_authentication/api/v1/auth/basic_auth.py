#!/usr/bin/env python3
""" a module that for basic authentication
"""

from .auth import Auth
import base64


class BasicAuth(Auth):
    """ a basic authentication class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ enconcodes the authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]
