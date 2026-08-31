from typing import Literal

ApiV1BlocksUpdateSupportsHaErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateSupportsHaErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_update_supports_ha_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateSupportsHaErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
