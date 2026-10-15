from typing import Literal

HostSimpleKind = Literal["bare_metal", "vm"]

HOST_SIMPLE_KIND_VALUES: set[HostSimpleKind] = {
    "bare_metal",
    "vm",
}


def check_host_simple_kind(value: str) -> HostSimpleKind:
    if value in HOST_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_SIMPLE_KIND_VALUES!r}")
