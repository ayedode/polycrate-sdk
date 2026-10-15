from typing import Literal

RegionKind = Literal["generic"]

REGION_KIND_VALUES: set[RegionKind] = {
    "generic",
}


def check_region_kind(value: str) -> RegionKind:
    if value in REGION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_KIND_VALUES!r}")
