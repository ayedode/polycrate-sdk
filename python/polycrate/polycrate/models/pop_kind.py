from typing import Literal

PopKind = Literal["datacenter", "datacenter-park", "region"]

POP_KIND_VALUES: set[PopKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_pop_kind(value: str) -> PopKind:
    if value in POP_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_KIND_VALUES!r}")
