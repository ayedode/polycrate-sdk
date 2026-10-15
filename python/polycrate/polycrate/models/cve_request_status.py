from typing import Literal

CVERequestStatus = Literal["disputed", "open", "rejected", "reserved"]

CVE_REQUEST_STATUS_VALUES: set[CVERequestStatus] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_cve_request_status(value: str) -> CVERequestStatus:
    if value in CVE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_STATUS_VALUES!r}")
