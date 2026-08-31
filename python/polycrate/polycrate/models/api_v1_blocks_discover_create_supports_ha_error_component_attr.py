from typing import Literal

ApiV1BlocksDiscoverCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_BLOCKS_DISCOVER_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_blocks_discover_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateSupportsHaErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
