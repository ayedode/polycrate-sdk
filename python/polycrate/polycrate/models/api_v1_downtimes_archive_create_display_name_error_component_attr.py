from typing import Literal

ApiV1DowntimesArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_downtimes_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
