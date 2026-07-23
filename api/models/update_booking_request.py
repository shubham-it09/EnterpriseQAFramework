from dataclasses import asdict

from api.models.create_booking_request import CreateBookingRequest


def create_booking(
        self,
        request: CreateBookingRequest
):

    return self.client.post(
        "/booking",
        json=asdict(request)
    )