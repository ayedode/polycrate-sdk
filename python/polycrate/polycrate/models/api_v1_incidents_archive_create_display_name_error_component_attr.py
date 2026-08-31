from typing import Literal

ApiV1IncidentsArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_INCIDENTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_incidents_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
