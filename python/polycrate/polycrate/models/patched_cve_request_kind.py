from typing import Literal

PatchedCVERequestKind = Literal["generic"]

PATCHED_CVE_REQUEST_KIND_VALUES: set[PatchedCVERequestKind] = {
    "generic",
}


def check_patched_cve_request_kind(value: str) -> PatchedCVERequestKind:
    if value in PATCHED_CVE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_KIND_VALUES!r}")
