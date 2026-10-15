from typing import Literal

PatchedCVERequestSeverity = Literal["critical", "high", "low", "medium", "none", "unknown"]

PATCHED_CVE_REQUEST_SEVERITY_VALUES: set[PatchedCVERequestSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_patched_cve_request_severity(value: str) -> PatchedCVERequestSeverity:
    if value in PATCHED_CVE_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_SEVERITY_VALUES!r}")
