from typing import Literal

ApiV1IpaddressesArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_ipaddresses_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
