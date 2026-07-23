import pytest

from business.login_business import LoginBusiness


@pytest.fixture(scope="function")
def login_business(pw_page, logger):

    return LoginBusiness(
        pw_page,
        logger
    )