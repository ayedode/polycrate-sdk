from typing import Literal

PatchedDowntimeRequestSeverity = Literal["critical", "major", "minor"]

PATCHED_DOWNTIME_REQUEST_SEVERITY_VALUES: set[PatchedDowntimeRequestSeverity] = {
    "critical",
    "major",
    "minor",
}


def check_patched_downtime_request_severity(value: str) -> PatchedDowntimeRequestSeverity:
    if value in PATCHED_DOWNTIME_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DOWNTIME_REQUEST_SEVERITY_VALUES!r}")
