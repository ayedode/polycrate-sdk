from typing import Literal

ApiV1MaintenancesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenances_update_kind_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateKindErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
