from enum import Enum


class GetHistoricProcessInstanceDurationReportPeriodUnit(str, Enum):
    MONTH = "month"
    QUARTER = "quarter"

    def __str__(self) -> str:
        return str(self.value)
