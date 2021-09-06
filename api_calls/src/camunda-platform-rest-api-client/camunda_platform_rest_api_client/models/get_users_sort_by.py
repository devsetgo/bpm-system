from enum import Enum


class GetUsersSortBy(str, Enum):
    USERID = "userId"
    FIRSTNAME = "firstName"
    LASTNAME = "lastName"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
