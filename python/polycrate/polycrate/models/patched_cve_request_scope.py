from typing import Literal

PatchedCVERequestScope = Literal["system", "user"]

PATCHED_CVE_REQUEST_SCOPE_VALUES: set[PatchedCVERequestScope] = {
    "system",
    "user",
}


def check_patched_cve_request_scope(value: str) -> PatchedCVERequestScope:
    if value in PATCHED_CVE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_SCOPE_VALUES!r}")
