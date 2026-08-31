from typing import Literal

ApiV1AlertroutersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ALERTROUTERS_LIST_STATE_VALUES: set[ApiV1AlertroutersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_alertrouters_list_state(value: str) -> ApiV1AlertroutersListState:
    if value in API_V1_ALERTROUTERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_STATE_VALUES!r}")
