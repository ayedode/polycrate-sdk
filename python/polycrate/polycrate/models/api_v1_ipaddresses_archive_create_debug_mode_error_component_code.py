from typing import Literal

ApiV1IpaddressesArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_ipaddresses_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
