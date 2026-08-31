from typing import Literal

ApiV1MaintenanceWindowsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_MAINTENANCE_WINDOWS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_maintenance_windows_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
