from typing import Literal

ApiV1PopsArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pops_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PopsArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_POPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
