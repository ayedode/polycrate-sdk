from typing import Literal

ApiV1IncidentsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_INCIDENTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_incidents_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
