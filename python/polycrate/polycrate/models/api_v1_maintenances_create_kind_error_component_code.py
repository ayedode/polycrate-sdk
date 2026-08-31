from typing import Literal

ApiV1MaintenancesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenances_create_kind_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateKindErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
