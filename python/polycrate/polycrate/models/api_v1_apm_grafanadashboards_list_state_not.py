from typing import Literal

ApiV1ApmGrafanadashboardsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_NOT_VALUES: set[ApiV1ApmGrafanadashboardsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_apm_grafanadashboards_list_state_not(value: str) -> ApiV1ApmGrafanadashboardsListStateNot:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_NOT_VALUES!r}"
    )
