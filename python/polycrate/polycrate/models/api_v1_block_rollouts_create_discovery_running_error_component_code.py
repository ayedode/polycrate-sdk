from typing import Literal

ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_create_discovery_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateDiscoveryRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
