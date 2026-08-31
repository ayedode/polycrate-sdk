from typing import Literal

ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_maintenance_windows_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
