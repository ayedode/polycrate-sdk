from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponentAttr = Literal[
    "cached_active_maintenances_count"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponentAttr
] = {
    "cached_active_maintenances_count",
}


def check_api_v1_organizations_discover_create_cached_active_maintenances_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
