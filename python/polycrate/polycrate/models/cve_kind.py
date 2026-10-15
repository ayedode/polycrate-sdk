from typing import Literal

CVEKind = Literal["generic"]

CVE_KIND_VALUES: set[CVEKind] = {
    "generic",
}


def check_cve_kind(value: str) -> CVEKind:
    if value in CVE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_KIND_VALUES!r}")
