from typing import Literal

BootstrapStatusEnum = Literal["deprovisioning", "failed", "joining", "pending", "provisioning", "ready"]

BOOTSTRAP_STATUS_ENUM_VALUES: set[BootstrapStatusEnum] = {
    "deprovisioning",
    "failed",
    "joining",
    "pending",
    "provisioning",
    "ready",
}


def check_bootstrap_status_enum(value: str) -> BootstrapStatusEnum:
    if value in BOOTSTRAP_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BOOTSTRAP_STATUS_ENUM_VALUES!r}")
