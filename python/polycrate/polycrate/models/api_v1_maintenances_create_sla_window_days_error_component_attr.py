from typing import Literal

ApiV1MaintenancesCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_maintenances_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
