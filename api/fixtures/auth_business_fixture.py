import pytest

from api.business.auth_business import AuthBusiness


@pytest.fixture
def auth_business(api_client):

    return AuthBusiness(api_client)