from enum import Enum


class GetEventSubscriptionsCountEventType(str, Enum):
    MESSAGE = "message"
    SIGNAL = "signal"
    COMPENSATE = "compensate"
    CONDITIONAL = "conditional"

    def __str__(self) -> str:
        return str(self.value)
