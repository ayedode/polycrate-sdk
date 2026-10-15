from typing import Literal

LoadbalancerInstanceCreateRequestEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_CREATE_REQUEST_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceCreateRequestEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_create_request_engine_version(
    value: int,
) -> LoadbalancerInstanceCreateRequestEngineVersion:
    if value in LOADBALANCER_INSTANCE_CREATE_REQUEST_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_CREATE_REQUEST_ENGINE_VERSION_VALUES!r}"
    )
