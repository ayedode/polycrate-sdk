from typing import Literal

LoadbalancerInstanceUpdateRequestEngineVersion = Literal[1, 2]

LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES: set[LoadbalancerInstanceUpdateRequestEngineVersion] = {
    1,
    2,
}


def check_loadbalancer_instance_update_request_engine_version(
    value: int,
) -> LoadbalancerInstanceUpdateRequestEngineVersion:
    if value in LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES!r}"
    )
