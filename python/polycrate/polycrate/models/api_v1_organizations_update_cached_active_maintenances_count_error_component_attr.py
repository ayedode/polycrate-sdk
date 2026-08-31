from typing import Literal

ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponentAttr = Literal["cached_active_maintenances_count"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponentAttr
] = {
    "cached_active_maintenances_count",
}


def check_api_v1_organizations_update_cached_active_maintenances_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
