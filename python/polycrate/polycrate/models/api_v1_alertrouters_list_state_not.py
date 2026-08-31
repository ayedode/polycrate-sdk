from typing import Literal

ApiV1AlertroutersListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ALERTROUTERS_LIST_STATE_NOT_VALUES: set[ApiV1AlertroutersListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_alertrouters_list_state_not(value: str) -> ApiV1AlertroutersListStateNot:
    if value in API_V1_ALERTROUTERS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_STATE_NOT_VALUES!r}")
