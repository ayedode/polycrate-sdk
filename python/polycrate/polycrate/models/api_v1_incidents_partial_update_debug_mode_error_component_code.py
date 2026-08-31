from typing import Literal

ApiV1IncidentsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
