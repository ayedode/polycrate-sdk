from typing import Literal

ApiV1EndpointsArchiveCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_endpoints_archive_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateArchivedByErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
