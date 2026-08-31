from typing import Literal

ApiV1MaintenancesCreateStartErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesCreateStartErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_maintenances_create_start_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateStartErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_CODE_VALUES!r}"
    )
