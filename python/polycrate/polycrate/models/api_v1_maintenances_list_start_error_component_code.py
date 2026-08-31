from typing import Literal

ApiV1MaintenancesListStartErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_LIST_START_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesListStartErrorComponentCode] = {
    "invalid",
}


def check_api_v1_maintenances_list_start_error_component_code(
    value: str,
) -> ApiV1MaintenancesListStartErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_START_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_START_ERROR_COMPONENT_CODE_VALUES!r}"
    )
