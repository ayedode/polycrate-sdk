from typing import Literal

LoadbalancerInstanceUpdateEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_UPDATE_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceUpdateEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_update_engine_version(value: int) -> LoadbalancerInstanceUpdateEngineVersion:
    if value in LOADBALANCER_INSTANCE_UPDATE_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_UPDATE_ENGINE_VERSION_VALUES!r}"
    )
