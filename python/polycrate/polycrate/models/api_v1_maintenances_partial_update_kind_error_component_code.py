from typing import Literal

ApiV1MaintenancesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenances_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateKindErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
