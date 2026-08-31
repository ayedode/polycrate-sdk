from typing import Literal

ApiV1MaintenancesPartialUpdateEndErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateEndErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_maintenances_partial_update_end_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateEndErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_END_ERROR_COMPONENT_CODE_VALUES!r}"
    )
