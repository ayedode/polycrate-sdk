from typing import Literal

ApiV1BlocksUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_blocks_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
