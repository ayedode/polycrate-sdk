from typing import Literal

ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponentAttr = Literal["cached_endpoint_down_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponentAttr
] = {
    "cached_endpoint_down_count",
}


def check_api_v1_organizations_archive_create_cached_endpoint_down_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
