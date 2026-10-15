from typing import Literal

RegionRequestScope = Literal["system", "user"]

REGION_REQUEST_SCOPE_VALUES: set[RegionRequestScope] = {
    "system",
    "user",
}


def check_region_request_scope(value: str) -> RegionRequestScope:
    if value in REGION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_REQUEST_SCOPE_VALUES!r}")
