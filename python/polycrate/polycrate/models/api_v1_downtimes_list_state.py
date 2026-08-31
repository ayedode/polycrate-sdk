from typing import Literal

ApiV1DowntimesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOWNTIMES_LIST_STATE_VALUES: set[ApiV1DowntimesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_downtimes_list_state(value: str) -> ApiV1DowntimesListState:
    if value in API_V1_DOWNTIMES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_STATE_VALUES!r}")
