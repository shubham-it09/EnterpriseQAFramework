"""
Module:
    test_patch_booking.py

Description:
    Verify booking can be partially updated.

Author:
    Shubham Pandey
"""

from core.file_utils import FileUtils
from api.models.create_booking_request import (
    CreateBookingRequest
)



def test_patch_booking(
        booking_business,
        auth_business
):
    """
    Verify booking can be partially updated.
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
    # Arrange - Patch Payload
    # -------------------------------------------------

    patch_payload = FileUtils.read_json(
        "testdata/api/patch_booking.json"
    )

    # -------------------------------------------------
    # Act
    # -------------------------------------------------

    patch_response = booking_business.patch_booking(
        booking_id,
        patch_payload,
        headers
    )

    assert patch_response.status_code == 200

    # -------------------------------------------------
    # Assert
    # -------------------------------------------------

    get_response = booking_business.get_booking(
        booking_id
    )

    assert get_response.status_code == 200

    booking = get_response.json()

    # Updated fields

    assert (
        booking["firstname"]
        == patch_payload["firstname"]
    )

    assert (
        booking["additionalneeds"]
        == patch_payload["additionalneeds"]
    )

    # Unchanged fields

    assert (
        booking["lastname"]
        == create_request.lastname
    )

    assert (
        booking["totalprice"]
        == create_request.totalprice
    )

    assert (
        booking["depositpaid"]
        == create_request.depositpaid
    )

    assert (
        booking["bookingdates"]["checkin"]
        == create_request.bookingdates.checkin
    )

    assert (
        booking["bookingdates"]["checkout"]
        == create_request.bookingdates.checkout
    )