from typing import Literal

ApiV1BlocksUpdateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateSupportsHaErrorComponentAttr] = {
    "supports_ha",
}


def check_api_v1_blocks_update_supports_ha_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateSupportsHaErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
