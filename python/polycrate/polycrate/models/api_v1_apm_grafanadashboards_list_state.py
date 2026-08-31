from typing import Literal

ApiV1ApmGrafanadashboardsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_VALUES: set[ApiV1ApmGrafanadashboardsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_apm_grafanadashboards_list_state(value: str) -> ApiV1ApmGrafanadashboardsListState:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_VALUES!r}")
