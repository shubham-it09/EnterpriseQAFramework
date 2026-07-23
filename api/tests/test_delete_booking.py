"""
Module:
    test_delete_booking.py

Description:
    Verify booking can be deleted successfully.

Author:
    Shubham Pandey
"""

from core.file_utils import FileUtils

from api.models.create_booking_request import (
    CreateBookingRequest
)


def test_delete_booking(
        booking_business,
        auth_business
):
    """
    Verify booking can be deleted successfully.
    """

    # -------------------------------------------------
    # Arrange - Create Booking
    # -------------------------------------------------

    create_payload = FileUtils.read_json(
        "testdata/api/create_booking.json"
    )

    create_request = CreateBookingRequest.from_dict(
        create_payload
    )

    create_response = booking_business.create_booking(
        create_request
    )

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    # -------------------------------------------------
    # Arrange - Authentication
    # -------------------------------------------------

    headers = auth_business.get_auth_headers()

    # -------------------------------------------------
    # Act - Delete Booking
    # -------------------------------------------------

    delete_response = booking_business.delete_booking(
        booking_id,
        headers
    )

    # -------------------------------------------------
    # Assert
    # -------------------------------------------------

    assert delete_response.status_code == 201

    # -------------------------------------------------
    # Verify Booking No Longer Exists
    # -------------------------------------------------

    get_response = booking_business.get_booking(
        booking_id
    )

    assert get_response.status_code == 404