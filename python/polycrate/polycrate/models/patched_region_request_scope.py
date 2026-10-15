from typing import Literal

PatchedRegionRequestScope = Literal["system", "user"]

PATCHED_REGION_REQUEST_SCOPE_VALUES: set[PatchedRegionRequestScope] = {
    "system",
    "user",
}


def check_patched_region_request_scope(value: str) -> PatchedRegionRequestScope:
    if value in PATCHED_REGION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_REGION_REQUEST_SCOPE_VALUES!r}")
