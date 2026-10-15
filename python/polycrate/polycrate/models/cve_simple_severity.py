from typing import Literal

CVESimpleSeverity = Literal["critical", "high", "low", "medium", "none", "unknown"]

CVE_SIMPLE_SEVERITY_VALUES: set[CVESimpleSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_cve_simple_severity(value: str) -> CVESimpleSeverity:
    if value in CVE_SIMPLE_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_SIMPLE_SEVERITY_VALUES!r}")
