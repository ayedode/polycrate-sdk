from typing import Literal

LoadbalancerInstanceDeploymentStrategy = Literal["blue_green", "canary", "rolling"]

LOADBALANCER_INSTANCE_DEPLOYMENT_STRATEGY_VALUES: set[LoadbalancerInstanceDeploymentStrategy] = {
    "blue_green",
    "canary",
    "rolling",
}


def check_loadbalancer_instance_deployment_strategy(value: str) -> LoadbalancerInstanceDeploymentStrategy:
    if value in LOADBALANCER_INSTANCE_DEPLOYMENT_STRATEGY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_DEPLOYMENT_STRATEGY_VALUES!r}")
