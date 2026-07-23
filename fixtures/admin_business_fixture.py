import pytest

from business.admin_business import AdminBusiness


@pytest.fixture(scope="function")
def admin_business(
        pw_page,
        logger):

    return AdminBusiness(
        pw_page,
        logger
    )