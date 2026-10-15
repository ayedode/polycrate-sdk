from typing import Literal

CVESimpleStatus = Literal["disputed", "open", "rejected", "reserved"]

CVE_SIMPLE_STATUS_VALUES: set[CVESimpleStatus] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_cve_simple_status(value: str) -> CVESimpleStatus:
    if value in CVE_SIMPLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_SIMPLE_STATUS_VALUES!r}")
