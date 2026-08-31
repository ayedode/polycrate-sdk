from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
