from enum import Enum


class RestartProcessInstanceModificationInstructionDtoType(str, Enum):
    STARTBEFOREACTIVITY = "startBeforeActivity"
    STARTAFTERACTIVITY = "startAfterActivity"
    STARTTRANSITION = "startTransition"

    def __str__(self) -> str:
        return str(self.value)
