from typing import Literal

LoadbalancerInstanceListEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_LIST_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceListEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_list_engine_version(value: int) -> LoadbalancerInstanceListEngineVersion:
    if value in LOADBALANCER_INSTANCE_LIST_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LIST_ENGINE_VERSION_VALUES!r}")
