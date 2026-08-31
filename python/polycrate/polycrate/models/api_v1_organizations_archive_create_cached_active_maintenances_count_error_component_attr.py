from typing import Literal

ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponentAttr = Literal[
    "cached_active_maintenances_count"
]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponentAttr
] = {
    "cached_active_maintenances_count",
}


def check_api_v1_organizations_archive_create_cached_active_maintenances_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
