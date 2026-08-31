from typing import Literal

ApiV1MaintenancesCreateSlaWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateSlaWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_maintenances_create_sla_window_days_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateSlaWindowDaysErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
