from api.endpoints.auth_endpoint import AuthEndpoint
from api.models.auth_request import AuthRequest
from core.file_utils import FileUtils


class AuthBusiness:

    def __init__(self, api_client):

        self.auth_endpoint = AuthEndpoint(api_client)

    def authenticate(
            self,
            request: AuthRequest
    ):

        return self.auth_endpoint.authenticate(request)

    def get_token(self) -> str:
        """
        Returns authentication token.
        """

        payload = FileUtils.read_json(
            "testdata/api/auth.json"
        )

        request = AuthRequest.from_dict(
            payload
        )
        response = self.authenticate(request)
        return response.json()["token"]

    def get_auth_headers(self) -> dict:
        """
        Returns authentication headers.
           """
        token = self.get_token()

        return {
            "Cookie": f"token={token}"
        }