from typing import Literal

DelegationSourceEnum = Literal["loopback_lb", "loopback_object_store"]

DELEGATION_SOURCE_ENUM_VALUES: set[DelegationSourceEnum] = {
    "loopback_lb",
    "loopback_object_store",
}


def check_delegation_source_enum(value: str) -> DelegationSourceEnum:
    if value in DELEGATION_SOURCE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATION_SOURCE_ENUM_VALUES!r}")
