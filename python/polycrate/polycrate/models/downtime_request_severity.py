from typing import Literal

DowntimeRequestSeverity = Literal["critical", "major", "minor"]

DOWNTIME_REQUEST_SEVERITY_VALUES: set[DowntimeRequestSeverity] = {
    "critical",
    "major",
    "minor",
}


def check_downtime_request_severity(value: str) -> DowntimeRequestSeverity:
    if value in DOWNTIME_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_REQUEST_SEVERITY_VALUES!r}")
