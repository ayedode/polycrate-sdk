from typing import Literal

ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_DISCOVER_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_discover_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
