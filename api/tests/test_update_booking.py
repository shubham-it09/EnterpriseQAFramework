"""
Module:
    test_update_booking.py

Description:
    Verify an existing booking can be updated successfully.

Author:
    Shubham Pandey
"""

from core.file_utils import FileUtils

from api.models.create_booking_request import (
    CreateBookingRequest
)


def test_update_booking(
        booking_business,
        auth_business
):
    """
    Verify booking can be updated successfully.
    """

    # ------------------------------------------
    # Arrange - Create Booking
    # ------------------------------------------

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
    print("################  booking id ################# \n",booking_id)

    # ------------------------------------------
    # Arrange - Authentication
    # ------------------------------------------

    headers = auth_business.get_auth_headers()

    print("################  Header ################# \n",headers)

    # ------------------------------------------
    # Arrange - Updated Data
    # ------------------------------------------

    update_payload = FileUtils.read_json(
        "testdata/api/update_booking.json"
    )

    update_request = CreateBookingRequest.from_dict(
        update_payload
    )

    # ------------------------------------------
    # Act - Update Booking
    # ------------------------------------------

    update_response = booking_business.update_booking(
        booking_id,
        update_request,
        headers
    )

    # ------------------------------------------
    # Assert - Update Response
    # ------------------------------------------

    assert update_response.status_code == 200

    updated_booking = update_response.json()

    assert updated_booking["firstname"] == update_request.firstname

    assert updated_booking["lastname"] == update_request.lastname

    assert updated_booking["totalprice"] == update_request.totalprice

    assert (
        updated_booking["depositpaid"]
        == update_request.depositpaid
    )

    # ------------------------------------------
    # Assert - Verify Booking Using GET
    # ------------------------------------------

    get_response = booking_business.get_booking(
        booking_id
    )

    assert get_response.status_code == 200

    booking = get_response.json()

    assert booking["firstname"] == update_request.firstname

    assert booking["lastname"] == update_request.lastname

    assert booking["totalprice"] == update_request.totalprice

    assert (
        booking["depositpaid"]
        == update_request.depositpaid
    )

    assert (
        booking["bookingdates"]["checkin"]
        == update_request.bookingdates.checkin
    )

    assert (
        booking["bookingdates"]["checkout"]
        == update_request.bookingdates.checkout
    )

    assert (
        booking["additionalneeds"]
        == update_request.additionalneeds
    )