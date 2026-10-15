from typing import Literal

PatchedRegionRequestKind = Literal["generic"]

PATCHED_REGION_REQUEST_KIND_VALUES: set[PatchedRegionRequestKind] = {
    "generic",
}


def check_patched_region_request_kind(value: str) -> PatchedRegionRequestKind:
    if value in PATCHED_REGION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_REGION_REQUEST_KIND_VALUES!r}")
