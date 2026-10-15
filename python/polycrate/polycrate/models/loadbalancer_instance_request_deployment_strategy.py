from typing import Literal

LoadbalancerInstanceRequestDeploymentStrategy = Literal["blue_green", "canary", "rolling"]

LOADBALANCER_INSTANCE_REQUEST_DEPLOYMENT_STRATEGY_VALUES: set[LoadbalancerInstanceRequestDeploymentStrategy] = {
    "blue_green",
    "canary",
    "rolling",
}


def check_loadbalancer_instance_request_deployment_strategy(
    value: str,
) -> LoadbalancerInstanceRequestDeploymentStrategy:
    if value in LOADBALANCER_INSTANCE_REQUEST_DEPLOYMENT_STRATEGY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_DEPLOYMENT_STRATEGY_VALUES!r}"
    )
