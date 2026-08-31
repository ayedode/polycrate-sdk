from typing import Literal

ApiV1MaintenanceWindowsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_MAINTENANCE_WINDOWS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_maintenance_windows_list_organizations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsListOrganizationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
