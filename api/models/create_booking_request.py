from dataclasses import dataclass

from api.models.booking_dates import BookingDates


@dataclass
class CreateBookingRequest:

    firstname: str

    lastname: str

    totalprice: int

    depositpaid: bool

    bookingdates: BookingDates

    additionalneeds: str

    @classmethod
    def from_dict(cls, data: dict):

        return cls(
            firstname=data["firstname"],
            lastname=data["lastname"],
            totalprice=data["totalprice"],
            depositpaid=data["depositpaid"],
            bookingdates=BookingDates.from_dict(
                data["bookingdates"]
            ),
            additionalneeds=data["additionalneeds"]
        )