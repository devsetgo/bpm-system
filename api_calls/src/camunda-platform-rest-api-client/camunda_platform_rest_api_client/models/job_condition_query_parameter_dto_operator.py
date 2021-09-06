from enum import Enum


class JobConditionQueryParameterDtoOperator(str, Enum):
    GT = "gt"
    LT = "lt"

    def __str__(self) -> str:
        return str(self.value)
