from typing import Literal

CVEScope = Literal["system", "user"]

CVE_SCOPE_VALUES: set[CVEScope] = {
    "system",
    "user",
}


def check_cve_scope(value: str) -> CVEScope:
    if value in CVE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_SCOPE_VALUES!r}")
