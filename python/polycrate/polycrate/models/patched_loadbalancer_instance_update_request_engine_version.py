from typing import Literal

PatchedLoadbalancerInstanceUpdateRequestEngineVersion = Literal[1, 2]

PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES: set[
    PatchedLoadbalancerInstanceUpdateRequestEngineVersion
] = {
    1,
    2,
}


def check_patched_loadbalancer_instance_update_request_engine_version(
    value: int,
) -> PatchedLoadbalancerInstanceUpdateRequestEngineVersion:
    if value in PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_ENGINE_VERSION_VALUES!r}"
    )
