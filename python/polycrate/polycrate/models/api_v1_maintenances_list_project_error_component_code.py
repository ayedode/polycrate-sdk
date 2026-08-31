from typing import Literal

ApiV1MaintenancesListProjectErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_LIST_PROJECT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesListProjectErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_maintenances_list_project_error_component_code(
    value: str,
) -> ApiV1MaintenancesListProjectErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_PROJECT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_PROJECT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
