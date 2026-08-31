from typing import Literal

ApiV1ActivitiesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ACTIVITIES_LIST_STATE_NOT_VALUES: set[ApiV1ActivitiesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_activities_list_state_not(value: str) -> ApiV1ActivitiesListStateNot:
    if value in API_V1_ACTIVITIES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_STATE_NOT_VALUES!r}")
