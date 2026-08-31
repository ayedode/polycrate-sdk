from typing import Literal

DowntimeSeverityEnum = Literal["critical", "major", "minor"]

DOWNTIME_SEVERITY_ENUM_VALUES: set[DowntimeSeverityEnum] = {
    "critical",
    "major",
    "minor",
}


def check_downtime_severity_enum(value: str) -> DowntimeSeverityEnum:
    if value in DOWNTIME_SEVERITY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_SEVERITY_ENUM_VALUES!r}")
