from enum import Enum


class DurationReportResultDtoPeriodUnit(str, Enum):
    MONTH = "MONTH"
    QUARTER = "QUARTER"

    def __str__(self) -> str:
        return str(self.value)
