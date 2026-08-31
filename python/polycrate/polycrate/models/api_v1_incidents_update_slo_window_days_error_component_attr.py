from typing import Literal

ApiV1IncidentsUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_INCIDENTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_incidents_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
