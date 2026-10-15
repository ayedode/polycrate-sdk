from typing import Literal

CVERequestScope = Literal["system", "user"]

CVE_REQUEST_SCOPE_VALUES: set[CVERequestScope] = {
    "system",
    "user",
}


def check_cve_request_scope(value: str) -> CVERequestScope:
    if value in CVE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_SCOPE_VALUES!r}")
