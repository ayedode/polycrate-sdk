from typing import Literal

ApiV1RegionsArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_REGIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_regions_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
