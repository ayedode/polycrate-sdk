from typing import Literal

ApiV1PrefixesArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PrefixesArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
