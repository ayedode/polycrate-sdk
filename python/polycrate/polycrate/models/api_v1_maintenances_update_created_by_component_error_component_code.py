from typing import Literal

ApiV1MaintenancesUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
