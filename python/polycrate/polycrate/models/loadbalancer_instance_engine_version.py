from typing import Literal

LoadbalancerInstanceEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_engine_version(value: int) -> LoadbalancerInstanceEngineVersion:
    if value in LOADBALANCER_INSTANCE_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_ENGINE_VERSION_VALUES!r}")
