from enum import Enum


class ProcessInstanceModificationInstructionDtoType(str, Enum):
    CANCEL = "cancel"
    STARTBEFOREACTIVITY = "startBeforeActivity"
    STARTAFTERACTIVITY = "startAfterActivity"
    STARTTRANSITION = "startTransition"

    def __str__(self) -> str:
        return str(self.value)
