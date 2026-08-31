from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentAttr = Literal["cached_open_incidents_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentAttr
] = {
    "cached_open_incidents_count",
}


def check_api_v1_organizations_icon_upload_create_cached_open_incidents_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
