from enum import Enum


class MultiFormVariableBinaryDtoValueType(str, Enum):
    BYTES = "Bytes"
    FILE = "File"

    def __str__(self) -> str:
        return str(self.value)
