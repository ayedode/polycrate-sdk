from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_icon_upload_create_cached_open_incidents_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
