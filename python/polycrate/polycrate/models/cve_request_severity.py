from typing import Literal

CVERequestSeverity = Literal["critical", "high", "low", "medium", "none", "unknown"]

CVE_REQUEST_SEVERITY_VALUES: set[CVERequestSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_cve_request_severity(value: str) -> CVERequestSeverity:
    if value in CVE_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_SEVERITY_VALUES!r}")
