from typing import Literal

HostRequestRole = Literal["", "generic", "k8s-controlplane", "k8s-worker"]

HOST_REQUEST_ROLE_VALUES: set[HostRequestRole] = {
    "",
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_host_request_role(value: str) -> HostRequestRole:
    if value in HOST_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_ROLE_VALUES!r}")
