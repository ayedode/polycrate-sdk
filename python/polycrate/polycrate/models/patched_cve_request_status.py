from typing import Literal

PatchedCVERequestStatus = Literal["disputed", "open", "rejected", "reserved"]

PATCHED_CVE_REQUEST_STATUS_VALUES: set[PatchedCVERequestStatus] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_patched_cve_request_status(value: str) -> PatchedCVERequestStatus:
    if value in PATCHED_CVE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_STATUS_VALUES!r}")
