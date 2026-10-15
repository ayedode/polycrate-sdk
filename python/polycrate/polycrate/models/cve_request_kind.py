from typing import Literal

CVERequestKind = Literal["generic"]

CVE_REQUEST_KIND_VALUES: set[CVERequestKind] = {
    "generic",
}


def check_cve_request_kind(value: str) -> CVERequestKind:
    if value in CVE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_KIND_VALUES!r}")
