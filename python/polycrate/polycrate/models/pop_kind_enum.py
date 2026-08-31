from typing import Literal

PopKindEnum = Literal["datacenter", "datacenter-park", "region"]

POP_KIND_ENUM_VALUES: set[PopKindEnum] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_pop_kind_enum(value: str) -> PopKindEnum:
    if value in POP_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_KIND_ENUM_VALUES!r}")
