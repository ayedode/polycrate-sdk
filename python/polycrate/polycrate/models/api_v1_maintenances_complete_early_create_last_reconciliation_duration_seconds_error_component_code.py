from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length"
]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_maintenances_complete_early_create_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponentCode:
    if (
        value
        in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
