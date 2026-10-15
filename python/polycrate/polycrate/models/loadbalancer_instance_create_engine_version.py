from typing import Literal

LoadbalancerInstanceCreateEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_CREATE_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceCreateEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_create_engine_version(value: int) -> LoadbalancerInstanceCreateEngineVersion:
    if value in LOADBALANCER_INSTANCE_CREATE_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_CREATE_ENGINE_VERSION_VALUES!r}"
    )
