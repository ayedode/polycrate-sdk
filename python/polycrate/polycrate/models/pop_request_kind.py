from typing import Literal

PopRequestKind = Literal["datacenter", "datacenter-park", "region"]

POP_REQUEST_KIND_VALUES: set[PopRequestKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_pop_request_kind(value: str) -> PopRequestKind:
    if value in POP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_KIND_VALUES!r}")
