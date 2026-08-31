from typing import Literal

ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_blocks_run_discovery_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
