from dataclasses import dataclass


@dataclass
class AuthRequest:

    username: str

    password: str

    @classmethod
    def from_dict(cls, data: dict):

        return cls(
            username=data["username"],
            password=data["password"]
        )