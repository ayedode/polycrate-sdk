from typing import Literal

ApiV1MaintenancesListEndErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_LIST_END_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesListEndErrorComponentCode] = {
    "invalid",
}


def check_api_v1_maintenances_list_end_error_component_code(value: str) -> ApiV1MaintenancesListEndErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_END_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_END_ERROR_COMPONENT_CODE_VALUES!r}"
    )
