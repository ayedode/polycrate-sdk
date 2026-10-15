from typing import Literal

HostKind = Literal["bare_metal", "vm"]

HOST_KIND_VALUES: set[HostKind] = {
    "bare_metal",
    "vm",
}


def check_host_kind(value: str) -> HostKind:
    if value in HOST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_KIND_VALUES!r}")
