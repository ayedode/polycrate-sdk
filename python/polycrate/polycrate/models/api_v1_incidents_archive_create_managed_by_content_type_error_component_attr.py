from typing import Literal

ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_INCIDENTS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_incidents_archive_create_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
