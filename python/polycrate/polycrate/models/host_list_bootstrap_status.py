from typing import Literal

HostListBootstrapStatus = Literal["deprovisioning", "failed", "joining", "pending", "provisioning", "ready"]

HOST_LIST_BOOTSTRAP_STATUS_VALUES: set[HostListBootstrapStatus] = {
    "deprovisioning",
    "failed",
    "joining",
    "pending",
    "provisioning",
    "ready",
}


def check_host_list_bootstrap_status(value: str) -> HostListBootstrapStatus:
    if value in HOST_LIST_BOOTSTRAP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_LIST_BOOTSTRAP_STATUS_VALUES!r}")
