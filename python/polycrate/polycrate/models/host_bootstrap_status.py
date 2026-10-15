from typing import Literal

HostBootstrapStatus = Literal["deprovisioning", "failed", "joining", "pending", "provisioning", "ready"]

HOST_BOOTSTRAP_STATUS_VALUES: set[HostBootstrapStatus] = {
    "deprovisioning",
    "failed",
    "joining",
    "pending",
    "provisioning",
    "ready",
}


def check_host_bootstrap_status(value: str) -> HostBootstrapStatus:
    if value in HOST_BOOTSTRAP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_BOOTSTRAP_STATUS_VALUES!r}")
