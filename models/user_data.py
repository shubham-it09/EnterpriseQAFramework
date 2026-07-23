from dataclasses import dataclass


@dataclass
class UserData:
    """
    Represents a User in OrangeHRM.
    """

    role: str
    employee_name: str
    status: str
    username: str
    password: str