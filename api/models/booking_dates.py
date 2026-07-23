from dataclasses import dataclass


@dataclass
class BookingDates:

    checkin: str

    checkout: str

    @classmethod
    def from_dict(cls, data: dict):

        return cls(
            checkin=data["checkin"],
            checkout=data["checkout"]
        )