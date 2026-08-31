from typing import Literal

ApiV1EndpointsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ENDPOINTS_LIST_STATE_VALUES: set[ApiV1EndpointsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_endpoints_list_state(value: str) -> ApiV1EndpointsListState:
    if value in API_V1_ENDPOINTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_STATE_VALUES!r}")
