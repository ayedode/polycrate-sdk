from typing import Literal

ApiV1IncidentsUpdateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_incidents_update_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
