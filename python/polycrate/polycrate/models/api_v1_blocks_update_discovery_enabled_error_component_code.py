from typing import Literal

ApiV1BlocksUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
