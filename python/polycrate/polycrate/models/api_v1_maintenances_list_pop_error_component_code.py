from typing import Literal

ApiV1MaintenancesListPopErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesListPopErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_maintenances_list_pop_error_component_code(value: str) -> ApiV1MaintenancesListPopErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
