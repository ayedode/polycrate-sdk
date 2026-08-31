from typing import Literal

ApiV1MaintenanceWindowsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_maintenance_windows_update_archived_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateArchivedErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
