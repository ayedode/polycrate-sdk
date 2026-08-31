from typing import Literal

ApiV1EndpointsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ENDPOINTS_LIST_STATE_NOT_VALUES: set[ApiV1EndpointsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_endpoints_list_state_not(value: str) -> ApiV1EndpointsListStateNot:
    if value in API_V1_ENDPOINTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_STATE_NOT_VALUES!r}")
