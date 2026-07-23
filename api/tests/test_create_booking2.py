from core.file_utils import FileUtils

from api.models.create_booking_request import (
    CreateBookingRequest
)


def test_create_booking(
        booking_business
):
    """
    Verify booking can be created successfully.
    """

    payload = FileUtils.read_json(
        "testdata/api/create_booking.json"
    )

    request = CreateBookingRequest.from_dict(
        payload
    )

    response = booking_business.create_booking(
        request
    )

    assert response.status_code == 200

    response_json = response.json()

    assert "bookingid" in response_json

    assert isinstance(
        response_json["bookingid"],
        int
    )

    booking = response_json["booking"]

    assert booking["firstname"] == request.firstname

    assert booking["lastname"] == request.lastname

    assert booking["totalprice"] == request.totalprice

    assert booking["depositpaid"] == request.depositpaid