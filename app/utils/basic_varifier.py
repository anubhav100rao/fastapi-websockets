from fastapi import Depends
from fastapi import FastAPI
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from uuid import UUID
from fastapi_sessions.backends.implementations import InMemoryBackend
from uuid import uuid4
from fastapi import FastAPI, Response
from ..schemas import SessionData
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi import HTTPException


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True