from typing import Literal

RegionRequestKind = Literal["generic"]

REGION_REQUEST_KIND_VALUES: set[RegionRequestKind] = {
    "generic",
}


def check_region_request_kind(value: str) -> RegionRequestKind:
    if value in REGION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_REQUEST_KIND_VALUES!r}")
