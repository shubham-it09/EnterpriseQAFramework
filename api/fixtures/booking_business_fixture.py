import pytest

from api.business.booking_business import BookingBusiness


@pytest.fixture(scope="function")
def booking_business(api_client):
    """
    Creates Booking Business object.
    """

    return BookingBusiness(api_client)