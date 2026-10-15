from typing import Literal

HostSimpleRole = Literal["generic", "k8s-controlplane", "k8s-worker"]

HOST_SIMPLE_ROLE_VALUES: set[HostSimpleRole] = {
    "generic",
    "k8s-controlplane",
    "k8s-worker",
}


def check_host_simple_role(value: str) -> HostSimpleRole:
    if value in HOST_SIMPLE_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_SIMPLE_ROLE_VALUES!r}")
