from typing import Literal

HostListRole = Literal["generic", "k8s-controlplane", "k8s-worker"]

HOST_LIST_ROLE_VALUES: set[HostListRole] = {
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_host_list_role(value: str) -> HostListRole:
    if value in HOST_LIST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_LIST_ROLE_VALUES!r}")
