from typing import Literal

ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
