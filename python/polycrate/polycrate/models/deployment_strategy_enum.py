from typing import Literal

DeploymentStrategyEnum = Literal["blue_green", "canary", "rolling"]

DEPLOYMENT_STRATEGY_ENUM_VALUES: set[DeploymentStrategyEnum] = {
    "blue_green",
    "canary",
    "rolling",
}


def check_deployment_strategy_enum(value: str) -> DeploymentStrategyEnum:
    if value in DEPLOYMENT_STRATEGY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DEPLOYMENT_STRATEGY_ENUM_VALUES!r}")
