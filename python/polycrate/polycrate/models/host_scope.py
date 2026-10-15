from typing import Literal

HostScope = Literal["system", "user"]

HOST_SCOPE_VALUES: set[HostScope] = {
    "system",
    "user",
}


def check_host_scope(value: str) -> HostScope:
    if value in HOST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_SCOPE_VALUES!r}")
