from typing import Literal

RegionScope = Literal["system", "user"]

REGION_SCOPE_VALUES: set[RegionScope] = {
    "system",
    "user",
}


def check_region_scope(value: str) -> RegionScope:
    if value in REGION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_SCOPE_VALUES!r}")
