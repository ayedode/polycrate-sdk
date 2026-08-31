from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponentAttr = Literal["cached_open_incidents_count"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponentAttr
] = {
    "cached_open_incidents_count",
}


def check_api_v1_organizations_discover_create_cached_open_incidents_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
