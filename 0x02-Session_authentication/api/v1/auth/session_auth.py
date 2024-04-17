#!/usr/bin/env python3
""" a module for authentication mechanism
"""

from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ a session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ A function that creates a session id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id

        return session_id
