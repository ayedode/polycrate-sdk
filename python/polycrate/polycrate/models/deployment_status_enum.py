from typing import Literal

DeploymentStatusEnum = Literal["deployed", "deploying", "failed", "pending", "removing"]

DEPLOYMENT_STATUS_ENUM_VALUES: set[DeploymentStatusEnum] = {
    "deployed",
    "deploying",
    "failed",
    "pending",
    "removing",
}


def check_deployment_status_enum(value: str) -> DeploymentStatusEnum:
    if value in DEPLOYMENT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DEPLOYMENT_STATUS_ENUM_VALUES!r}")
