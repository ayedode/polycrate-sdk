from typing import Literal

HostSimpleBootstrapStatus = Literal["deprovisioning", "failed", "joining", "pending", "provisioning", "ready"]

HOST_SIMPLE_BOOTSTRAP_STATUS_VALUES: set[HostSimpleBootstrapStatus] = {
    "deprovisioning",
    "failed",
    "joining",
    "pending",
    "provisioning",
    "ready",
}


def check_host_simple_bootstrap_status(value: str) -> HostSimpleBootstrapStatus:
    if value in HOST_SIMPLE_BOOTSTRAP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_SIMPLE_BOOTSTRAP_STATUS_VALUES!r}")
