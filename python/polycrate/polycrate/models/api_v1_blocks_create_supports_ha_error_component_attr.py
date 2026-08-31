from typing import Literal

ApiV1BlocksCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_BLOCKS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateSupportsHaErrorComponentAttr] = {
    "supports_ha",
}


def check_api_v1_blocks_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateSupportsHaErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
