from typing import Literal

CVESeverity = Literal["critical", "high", "low", "medium", "none", "unknown"]

CVE_SEVERITY_VALUES: set[CVESeverity] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_cve_severity(value: str) -> CVESeverity:
    if value in CVE_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_SEVERITY_VALUES!r}")
