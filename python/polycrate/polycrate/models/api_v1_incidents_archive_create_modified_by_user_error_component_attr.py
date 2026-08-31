from typing import Literal

ApiV1IncidentsArchiveCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_INCIDENTS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_incidents_archive_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
