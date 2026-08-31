from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_complete_early_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
