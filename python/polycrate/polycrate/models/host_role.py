from typing import Literal

HostRole = Literal["", "generic", "k8s-controlplane", "k8s-worker"]

HOST_ROLE_VALUES: set[HostRole] = {
    "",
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_host_role(value: str) -> HostRole:
    if value in HOST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_ROLE_VALUES!r}")
