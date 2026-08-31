from typing import Literal

ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_partial_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
