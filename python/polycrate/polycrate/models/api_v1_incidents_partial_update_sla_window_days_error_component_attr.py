from typing import Literal

ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_INCIDENTS_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_incidents_partial_update_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
