from enum import Enum


class MessageCorrelationResultWithVariableDtoResultType(str, Enum):
    EXECUTION = "Execution"
    PROCESSDEFINITION = "ProcessDefinition"

    def __str__(self) -> str:
        return str(self.value)
