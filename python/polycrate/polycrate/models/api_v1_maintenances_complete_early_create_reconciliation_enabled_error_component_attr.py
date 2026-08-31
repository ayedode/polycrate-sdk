from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_maintenances_complete_early_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
