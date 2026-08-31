from typing import Literal

ApiV1RegionsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
