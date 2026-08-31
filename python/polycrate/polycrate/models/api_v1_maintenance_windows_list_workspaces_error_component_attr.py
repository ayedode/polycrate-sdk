from typing import Literal

ApiV1MaintenanceWindowsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_MAINTENANCE_WINDOWS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_maintenance_windows_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsListWorkspacesErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
