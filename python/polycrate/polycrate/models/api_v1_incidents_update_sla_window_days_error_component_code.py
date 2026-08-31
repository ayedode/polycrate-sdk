from typing import Literal

ApiV1IncidentsUpdateSlaWindowDaysErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateSlaWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_incidents_update_sla_window_days_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateSlaWindowDaysErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
