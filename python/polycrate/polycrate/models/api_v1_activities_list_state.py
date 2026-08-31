from typing import Literal

ApiV1ActivitiesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ACTIVITIES_LIST_STATE_VALUES: set[ApiV1ActivitiesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_activities_list_state(value: str) -> ApiV1ActivitiesListState:
    if value in API_V1_ACTIVITIES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_STATE_VALUES!r}")
