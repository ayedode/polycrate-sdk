from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_complete_early_create_criticality_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
