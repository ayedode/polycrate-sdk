from typing import Literal

ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1_MAINTENANCES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_maintenances_create_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
