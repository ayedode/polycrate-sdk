from typing import Literal

ApiV1BlocksPartialUpdateSupportsHaErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateSupportsHaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_partial_update_supports_ha_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateSupportsHaErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
