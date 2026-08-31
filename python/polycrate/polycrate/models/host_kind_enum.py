from typing import Literal

HostKindEnum = Literal["bare_metal", "vm"]

HOST_KIND_ENUM_VALUES: set[HostKindEnum] = {
    "bare_metal",
    "vm",
}


def check_host_kind_enum(value: str) -> HostKindEnum:
    if value in HOST_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_KIND_ENUM_VALUES!r}")
