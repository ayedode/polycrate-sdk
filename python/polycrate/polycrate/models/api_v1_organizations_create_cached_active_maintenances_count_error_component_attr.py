from typing import Literal

ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponentAttr = Literal["cached_active_maintenances_count"]

API_V1_ORGANIZATIONS_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponentAttr
] = {
    "cached_active_maintenances_count",
}


def check_api_v1_organizations_create_cached_active_maintenances_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
