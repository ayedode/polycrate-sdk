from typing import Literal

LoadbalancerInstanceRequestEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_REQUEST_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceRequestEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_request_engine_version(value: int) -> LoadbalancerInstanceRequestEngineVersion:
    if value in LOADBALANCER_INSTANCE_REQUEST_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_ENGINE_VERSION_VALUES!r}"
    )
