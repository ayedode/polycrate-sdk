from typing import Literal

ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
