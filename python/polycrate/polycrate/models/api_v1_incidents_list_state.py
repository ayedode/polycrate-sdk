from typing import Literal

ApiV1IncidentsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_INCIDENTS_LIST_STATE_VALUES: set[ApiV1IncidentsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_incidents_list_state(value: str) -> ApiV1IncidentsListState:
    if value in API_V1_INCIDENTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_STATE_VALUES!r}")
