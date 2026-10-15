from typing import Literal

HostRequestKind = Literal["bare_metal", "vm"]

HOST_REQUEST_KIND_VALUES: set[HostRequestKind] = {
    "bare_metal",
    "vm",
}


def check_host_request_kind(value: str) -> HostRequestKind:
    if value in HOST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_KIND_VALUES!r}")
