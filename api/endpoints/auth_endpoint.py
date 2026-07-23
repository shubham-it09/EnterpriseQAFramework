"""
Authentication endpoints.
"""

from dataclasses import asdict

from api.client.api_client import APIClient
from api.models.auth_request import AuthRequest


class AuthEndpoint:

    def __init__(
            self,
            api_client: APIClient
    ):

        self.client = api_client

    def authenticate(
            self,
            request: AuthRequest
    ):

        return self.client.post(
            "/auth",
            json=asdict(request)
        )