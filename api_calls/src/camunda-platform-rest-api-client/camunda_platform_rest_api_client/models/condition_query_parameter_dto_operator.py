from enum import Enum


class ConditionQueryParameterDtoOperator(str, Enum):
    EQ = "eq"
    NEQ = "neq"
    GT = "gt"
    GTEQ = "gteq"
    LT = "lt"
    LTEQ = "lteq"
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
