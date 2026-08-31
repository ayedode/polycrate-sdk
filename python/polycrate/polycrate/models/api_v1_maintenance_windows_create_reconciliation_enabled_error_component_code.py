from typing import Literal

ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
