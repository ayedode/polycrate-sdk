from typing import Literal

ApiV1SearchRetrieveState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_SEARCH_RETRIEVE_STATE_VALUES: set[ApiV1SearchRetrieveState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_search_retrieve_state(value: str) -> ApiV1SearchRetrieveState:
    if value in API_V1_SEARCH_RETRIEVE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SEARCH_RETRIEVE_STATE_VALUES!r}")
