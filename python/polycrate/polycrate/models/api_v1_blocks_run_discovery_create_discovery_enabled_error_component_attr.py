from typing import Literal

ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_blocks_run_discovery_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
