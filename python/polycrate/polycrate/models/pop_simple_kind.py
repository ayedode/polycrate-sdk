from typing import Literal

PopSimpleKind = Literal["datacenter", "datacenter-park", "region"]

POP_SIMPLE_KIND_VALUES: set[PopSimpleKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_pop_simple_kind(value: str) -> PopSimpleKind:
    if value in POP_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_SIMPLE_KIND_VALUES!r}")
