from typing import Literal

DowntimeSeverity = Literal["critical", "major", "minor"]

DOWNTIME_SEVERITY_VALUES: set[DowntimeSeverity] = {
    "critical",
    "major",
    "minor",
}


def check_downtime_severity(value: str) -> DowntimeSeverity:
    if value in DOWNTIME_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_SEVERITY_VALUES!r}")
