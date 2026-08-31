from typing import Literal

ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_incidents_archive_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
