from typing import Literal

CVEStatus = Literal["disputed", "open", "rejected", "reserved"]

CVE_STATUS_VALUES: set[CVEStatus] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_cve_status(value: str) -> CVEStatus:
    if value in CVE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_STATUS_VALUES!r}")
