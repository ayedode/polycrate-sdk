from typing import Literal

ApiV1MaintenancesListUntilErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesListUntilErrorComponentCode] = {
    "invalid",
}


def check_api_v1_maintenances_list_until_error_component_code(
    value: str,
) -> ApiV1MaintenancesListUntilErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
