from typing import Literal

ApiV1ConditionsArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1ConditionsArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
