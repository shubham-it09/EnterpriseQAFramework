from dataclasses import asdict
from api.models.create_booking_request import CreateBookingRequest

"""
Module:
    booking_endpoint.py

Description:
    Booking API endpoints.

Author:
    Shubham Pandey
"""

from api.client.api_client import APIClient
from dataclasses import asdict


class BookingEndpoint:

    def __init__(
            self,
            client: APIClient
    ):

        self.client = client
    
    def get_bookings(
        self,
        **params
    ):
        """
        Returns all bookings.
        """

        return self.client.get(
            "/booking",
            params=params
        )
    
    def create_booking(
        self,
        request: dict
    ):
        """
        Creates booking.
        """

        return self.client.post(
            "/booking",
            json=asdict(request)
        )
    
    def update_booking(
        self,
        booking_id: int,
        request: CreateBookingRequest,
        headers: dict
    ):

        return self.client.put(
            f"/booking/{booking_id}",
            json=asdict(request),
            headers=headers
        )
    
    def partial_update_booking(
        self,
        booking_id: int,
        payload: dict,
        headers: dict
    ):

        return self.client.patch(
            f"/booking/{booking_id}",
            json=payload,
            headers=headers
        )
    
    def delete_booking(
        self,
        booking_id: int,
        headers: dict
    ):

        return self.client.delete(
            f"/booking/{booking_id}",
            headers=headers
        )
    
    def get_booking(
        self,
        booking_id: int
    ):

        return self.client.get(
            f"/booking/{booking_id}"
        )
    def patch_booking(
            self,
            booking_id: int,
            payload: dict,
            headers: dict
    ):
        """
        Partially updates a booking.
        """

        return self.client.patch(
            f"/booking/{booking_id}",
            json=payload,
            headers=headers
        )
    def delete_booking(
            self,
            booking_id: int,
            headers: dict
    ):
        """
        Deletes a booking.
        """

        return self.client.delete(
            f"/booking/{booking_id}",
            headers=headers
        )