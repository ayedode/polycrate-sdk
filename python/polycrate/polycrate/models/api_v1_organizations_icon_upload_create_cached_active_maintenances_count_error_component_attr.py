from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponentAttr = Literal[
    "cached_active_maintenances_count"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponentAttr
] = {
    "cached_active_maintenances_count",
}


def check_api_v1_organizations_icon_upload_create_cached_active_maintenances_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_MAINTENANCES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
