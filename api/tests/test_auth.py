from core.file_utils import FileUtils

from api.models.auth_request import AuthRequest


def test_authentication(auth_business):

    payload = FileUtils.read_json(
        "testdata/api/auth.json"
    )

    request = AuthRequest.from_dict(payload)

    response = auth_business.authenticate(request)

    assert response.status_code == 200

    response_json = response.json()

    assert "token" in response_json

    assert isinstance(
        response_json["token"],
        str
    )

    assert len(response_json["token"]) > 0