from typing import Literal

LoadbalancerInstanceDeploymentDeploymentStatus = Literal["deployed", "deploying", "failed", "pending", "removing"]

LOADBALANCER_INSTANCE_DEPLOYMENT_DEPLOYMENT_STATUS_VALUES: set[LoadbalancerInstanceDeploymentDeploymentStatus] = {
    "deployed",
    "deploying",
    "failed",
    "pending",
    "removing",
}


def check_loadbalancer_instance_deployment_deployment_status(
    value: str,
) -> LoadbalancerInstanceDeploymentDeploymentStatus:
    if value in LOADBALANCER_INSTANCE_DEPLOYMENT_DEPLOYMENT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_DEPLOYMENT_DEPLOYMENT_STATUS_VALUES!r}"
    )
