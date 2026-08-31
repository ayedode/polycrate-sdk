from typing import Literal

ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_maintenance_windows_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
