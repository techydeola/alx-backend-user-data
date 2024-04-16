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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ a function that decodes base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            raw_data = base64.b64decode(base64_authorization_header,
                                        validate=True).decode('utf-8')
            return raw_data
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ returns the user email and password
            from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(":"))
