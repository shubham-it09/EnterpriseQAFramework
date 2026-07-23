"""
Module:
    booking_business.py

Description:
    Business layer for Booking APIs.
"""

from api.endpoints.booking_endpoint import BookingEndpoint
from api.models.create_booking_request import CreateBookingRequest


class BookingBusiness:

    def __init__(self, api_client):

        self.booking_endpoint = BookingEndpoint(api_client)

    def create_booking(
            self,
            request: CreateBookingRequest
    ):

        return self.booking_endpoint.create_booking(request)

    def get_booking(
            self,
            booking_id: int
    ):

        return self.booking_endpoint.get_booking(booking_id)

    def get_all_bookings(self, **params):

        return self.booking_endpoint.get_bookings(**params)
    
    def update_booking(self,booking_id: int,request: CreateBookingRequest,headers: dict):

        return self.booking_endpoint.update_booking(booking_id,request,headers)
    
    def patch_booking(self,booking_id: int,payload: dict,headers: dict):

        return self.booking_endpoint.patch_booking(
            booking_id,
            payload,
            headers
        )
    

    def delete_booking(self,booking_id: int,headers: dict):
        return self.booking_endpoint.delete_booking(
            booking_id,
            headers
        )